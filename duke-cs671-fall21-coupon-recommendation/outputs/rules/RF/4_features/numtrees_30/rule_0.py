def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[0]>0:
		# {"feature": "Education", "instances": 29, "metric_value": 0.9294, "depth": 2}
		if obj[1]>0:
			# {"feature": "Occupation", "instances": 19, "metric_value": 0.998, "depth": 3}
			if obj[2]<=12:
				# {"feature": "Distance", "instances": 18, "metric_value": 1.0, "depth": 4}
				if obj[3]<=2:
					return 'False'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			elif obj[2]>12:
				return 'True'
			else: return 'True'
		elif obj[1]<=0:
			# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[2]>5:
				return 'True'
			elif obj[2]<=5:
				# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=1:
					return 'False'
				elif obj[3]>1:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]<=0:
		# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 2}
		if obj[2]>1:
			return 'False'
		elif obj[2]<=1:
			return 'True'
		else: return 'True'
	else: return 'False'
