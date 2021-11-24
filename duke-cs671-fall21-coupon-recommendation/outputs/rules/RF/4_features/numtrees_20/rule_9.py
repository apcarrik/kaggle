def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[2]<=14:
		# {"feature": "Education", "instances": 48, "metric_value": 0.9987, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Distance", "instances": 46, "metric_value": 0.9945, "depth": 3}
			if obj[3]<=2:
				# {"feature": "Coupon", "instances": 39, "metric_value": 0.9995, "depth": 4}
				if obj[0]<=3:
					return 'False'
				elif obj[0]>3:
					return 'False'
				else: return 'False'
			elif obj[3]>2:
				# {"feature": "Coupon", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[0]<=3:
					return 'False'
				elif obj[0]>3:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[2]>14:
		return 'True'
	else: return 'True'
