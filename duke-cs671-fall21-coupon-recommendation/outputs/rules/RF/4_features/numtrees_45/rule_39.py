def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[2]<=15:
		# {"feature": "Distance", "instances": 22, "metric_value": 0.9024, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Education", "instances": 21, "metric_value": 0.8631, "depth": 3}
			if obj[1]>0:
				# {"feature": "Coupon", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[0]<=3:
					return 'True'
				elif obj[0]>3:
					return 'True'
				else: return 'True'
			elif obj[1]<=0:
				# {"feature": "Coupon", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[0]>2:
					return 'True'
				elif obj[0]<=2:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[3]>2:
			return 'False'
		else: return 'False'
	elif obj[2]>15:
		return 'False'
	else: return 'False'
