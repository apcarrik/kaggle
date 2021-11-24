def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9637, "depth": 1}
	if obj[0]>1:
		# {"feature": "Occupation", "instances": 56, "metric_value": 0.8384, "depth": 2}
		if obj[2]<=7:
			# {"feature": "Restaurant20to50", "instances": 41, "metric_value": 0.6594, "depth": 3}
			if obj[3]>-1.0:
				# {"feature": "Education", "instances": 40, "metric_value": 0.6098, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Distance", "instances": 36, "metric_value": 0.65, "depth": 5}
					if obj[4]<=2:
						return 'True'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				elif obj[1]>2:
					return 'True'
				else: return 'True'
			elif obj[3]<=-1.0:
				return 'False'
			else: return 'False'
		elif obj[2]>7:
			# {"feature": "Distance", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[4]<=1:
				# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[3]<=3.0:
					# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[1]>1:
						return 'True'
					elif obj[1]<=1:
						return 'True'
					else: return 'True'
				elif obj[3]>3.0:
					return 'False'
				else: return 'False'
			elif obj[4]>1:
				# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[3]<=1.0:
					return 'False'
				elif obj[3]>1.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Distance", "instances": 29, "metric_value": 0.9576, "depth": 2}
		if obj[4]<=2:
			# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 1.0, "depth": 3}
			if obj[3]<=1.0:
				# {"feature": "Occupation", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[2]>1:
					# {"feature": "Education", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[1]<=2:
						return 'False'
					elif obj[1]>2:
						return 'True'
					else: return 'True'
				elif obj[2]<=1:
					return 'False'
				else: return 'False'
			elif obj[3]>1.0:
				# {"feature": "Occupation", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[2]>1:
					# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[1]<=0:
						return 'True'
					elif obj[1]>0:
						return 'True'
					else: return 'True'
				elif obj[2]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[4]>2:
			return 'False'
		else: return 'False'
	else: return 'False'
