def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[11]<=2.0:
		# {"feature": "Education", "instances": 19, "metric_value": 0.8997, "depth": 2}
		if obj[7]>1:
			# {"feature": "Income", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[9]>0:
				return 'False'
			elif obj[9]<=0:
				# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]>0:
					return 'False'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[7]<=1:
			# {"feature": "Children", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[6]<=0:
				# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[5]>1:
					return 'False'
				elif obj[5]<=1:
					return 'True'
				else: return 'True'
			elif obj[6]>0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[11]>2.0:
		return 'True'
	else: return 'True'
