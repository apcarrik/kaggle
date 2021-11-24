def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Income", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[9]>2:
		# {"feature": "Time", "instances": 17, "metric_value": 0.6723, "depth": 2}
		if obj[1]>1:
			return 'True'
		elif obj[1]<=1:
			# {"feature": "Children", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[6]>0:
				return 'True'
			elif obj[6]<=0:
				# {"feature": "Coupon_validity", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3]<=0:
					return 'False'
				elif obj[3]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[9]<=2:
		# {"feature": "Coupon_validity", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[3]>0:
			return 'False'
		elif obj[3]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
