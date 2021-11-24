def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[2]<=15:
		# {"feature": "Education", "instances": 47, "metric_value": 0.9252, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Coupon", "instances": 40, "metric_value": 0.971, "depth": 3}
			if obj[0]<=3:
				# {"feature": "Distance", "instances": 23, "metric_value": 0.9321, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			elif obj[0]>3:
				# {"feature": "Distance", "instances": 17, "metric_value": 0.9975, "depth": 4}
				if obj[3]>1:
					return 'True'
				elif obj[3]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[1]>2:
			return 'True'
		else: return 'True'
	elif obj[2]>15:
		return 'False'
	else: return 'False'
