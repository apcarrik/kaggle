def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9899, "depth": 1}
	if obj[0]>1:
		# {"feature": "Occupation", "instances": 95, "metric_value": 0.971, "depth": 2}
		if obj[2]<=20:
			# {"feature": "Education", "instances": 94, "metric_value": 0.9671, "depth": 3}
			if obj[1]<=2:
				return 'True'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		elif obj[2]>20:
			return 'False'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Occupation", "instances": 32, "metric_value": 0.9887, "depth": 2}
		if obj[2]<=15:
			# {"feature": "Education", "instances": 30, "metric_value": 0.9968, "depth": 3}
			if obj[1]>0:
				return 'False'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		elif obj[2]>15:
			return 'False'
		else: return 'False'
	else: return 'False'
