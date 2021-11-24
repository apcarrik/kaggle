def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.4734, "depth": 1}
	if obj[0]>1:
		# {"feature": "Distance", "instances": 5886, "metric_value": 0.4619, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Occupation", "instances": 5298, "metric_value": 0.4575, "depth": 3}
			if obj[2]>0:
				# {"feature": "Education", "instances": 5233, "metric_value": 0.4588, "depth": 4}
				if obj[1]>1:
					return 'True'
				elif obj[1]<=1:
					return 'True'
				else: return 'True'
			elif obj[2]<=0:
				# {"feature": "Education", "instances": 65, "metric_value": 0.3011, "depth": 4}
				if obj[1]<=0:
					return 'True'
				elif obj[1]>0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[3]>2:
			# {"feature": "Education", "instances": 588, "metric_value": 0.4927, "depth": 3}
			if obj[1]<=4:
				# {"feature": "Occupation", "instances": 585, "metric_value": 0.4941, "depth": 4}
				if obj[2]<=7.473504273504274:
					return 'False'
				elif obj[2]>7.473504273504274:
					return 'False'
				else: return 'False'
			elif obj[1]>4:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Occupation", "instances": 2261, "metric_value": 0.4837, "depth": 2}
		if obj[2]>2.0328104328662784:
			# {"feature": "Education", "instances": 1794, "metric_value": 0.4892, "depth": 3}
			if obj[1]>0:
				# {"feature": "Distance", "instances": 1184, "metric_value": 0.4809, "depth": 4}
				if obj[3]<=2:
					return 'False'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[1]<=0:
				# {"feature": "Distance", "instances": 610, "metric_value": 0.4995, "depth": 4}
				if obj[3]<=2:
					return 'False'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[2]<=2.0328104328662784:
			# {"feature": "Education", "instances": 467, "metric_value": 0.4388, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Distance", "instances": 416, "metric_value": 0.4293, "depth": 4}
				if obj[3]<=2:
					return 'False'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[1]>3:
				# {"feature": "Distance", "instances": 51, "metric_value": 0.4457, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
