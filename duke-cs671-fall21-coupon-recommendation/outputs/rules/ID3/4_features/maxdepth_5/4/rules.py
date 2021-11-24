def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 8148, "metric_value": 0.4751, "depth": 1}
	if obj[0]>1:
		# {"feature": "Distance", "instances": 5867, "metric_value": 0.4642, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Occupation", "instances": 5275, "metric_value": 0.46, "depth": 3}
			if obj[2]>0:
				# {"feature": "Education", "instances": 5219, "metric_value": 0.4611, "depth": 4}
				if obj[1]>1:
					return 'True'
				elif obj[1]<=1:
					return 'True'
				else: return 'True'
			elif obj[2]<=0:
				# {"feature": "Education", "instances": 56, "metric_value": 0.3149, "depth": 4}
				if obj[1]<=0:
					return 'True'
				elif obj[1]>0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[3]>2:
			# {"feature": "Education", "instances": 592, "metric_value": 0.4879, "depth": 3}
			if obj[1]>0:
				# {"feature": "Occupation", "instances": 407, "metric_value": 0.4831, "depth": 4}
				if obj[2]>0:
					return 'False'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			elif obj[1]<=0:
				# {"feature": "Occupation", "instances": 185, "metric_value": 0.4881, "depth": 4}
				if obj[2]<=22:
					return 'True'
				elif obj[2]>22:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Occupation", "instances": 2281, "metric_value": 0.4847, "depth": 2}
		if obj[2]>2.070384793617607:
			# {"feature": "Education", "instances": 1816, "metric_value": 0.4893, "depth": 3}
			if obj[1]>0:
				# {"feature": "Distance", "instances": 1208, "metric_value": 0.482, "depth": 4}
				if obj[3]<=2:
					return 'False'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[1]<=0:
				# {"feature": "Distance", "instances": 608, "metric_value": 0.4999, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]<=2.070384793617607:
			# {"feature": "Education", "instances": 465, "metric_value": 0.4291, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Distance", "instances": 416, "metric_value": 0.4249, "depth": 4}
				if obj[3]<=2:
					return 'False'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[1]>3:
				# {"feature": "Distance", "instances": 49, "metric_value": 0.4286, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
