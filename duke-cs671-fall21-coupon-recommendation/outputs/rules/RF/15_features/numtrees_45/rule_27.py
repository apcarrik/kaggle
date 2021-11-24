def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[14]>1:
		# {"feature": "Coupon", "instances": 12, "metric_value": 0.8113, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Income", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[9]>2:
					return 'False'
				elif obj[9]<=2:
					return 'True'
				else: return 'True'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[2]>3:
			return 'False'
		else: return 'False'
	elif obj[14]<=1:
		# {"feature": "Age", "instances": 11, "metric_value": 0.4395, "depth": 2}
		if obj[5]>0:
			return 'True'
		elif obj[5]<=0:
			# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[1]<=2:
				return 'True'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
