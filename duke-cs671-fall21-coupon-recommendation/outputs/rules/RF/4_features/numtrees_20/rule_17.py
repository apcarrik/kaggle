def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 37, "metric_value": 0.9353, "depth": 2}
		if obj[1]>0:
			# {"feature": "Occupation", "instances": 29, "metric_value": 0.9784, "depth": 3}
			if obj[2]<=20:
				# {"feature": "Distance", "instances": 28, "metric_value": 0.9666, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			elif obj[2]>20:
				return 'False'
			else: return 'False'
		elif obj[1]<=0:
			# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[2]>5:
				return 'True'
			elif obj[2]<=5:
				# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]<=1:
					return 'True'
				elif obj[3]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Occupation", "instances": 14, "metric_value": 0.7496, "depth": 2}
		if obj[2]>4:
			return 'False'
		elif obj[2]<=4:
			# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[1]>1:
				# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			elif obj[1]<=1:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
