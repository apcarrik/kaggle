def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9924, "depth": 1}
	if obj[1]>0:
		# {"feature": "Passanger", "instances": 101, "metric_value": 0.9397, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Occupation", "instances": 60, "metric_value": 1.0, "depth": 3}
			if obj[3]<=11:
				# {"feature": "Education", "instances": 42, "metric_value": 0.9737, "depth": 4}
				if obj[2]>1:
					# {"feature": "Distance", "instances": 31, "metric_value": 0.9932, "depth": 5}
					if obj[5]>1:
						# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.9819, "depth": 6}
						if obj[4]<=2.0:
							return 'False'
						elif obj[4]>2.0:
							return 'True'
						else: return 'True'
					elif obj[5]<=1:
						# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.8113, "depth": 6}
						if obj[4]<=2.0:
							return 'True'
						elif obj[4]>2.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[2]<=1:
					# {"feature": "Distance", "instances": 11, "metric_value": 0.8454, "depth": 5}
					if obj[5]>1:
						return 'True'
					elif obj[5]<=1:
						# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[4]>0.0:
							return 'False'
						elif obj[4]<=0.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[3]>11:
				# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.8524, "depth": 4}
				if obj[4]<=3.0:
					# {"feature": "Education", "instances": 17, "metric_value": 0.7871, "depth": 5}
					if obj[2]>1:
						# {"feature": "Distance", "instances": 10, "metric_value": 0.8813, "depth": 6}
						if obj[5]<=1:
							return 'False'
						elif obj[5]>1:
							return 'False'
						else: return 'False'
					elif obj[2]<=1:
						# {"feature": "Distance", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[5]<=1:
							return 'False'
						elif obj[5]>1:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[4]>3.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[0]>1:
			# {"feature": "Occupation", "instances": 41, "metric_value": 0.6006, "depth": 3}
			if obj[3]>4:
				# {"feature": "Restaurant20to50", "instances": 27, "metric_value": 0.7642, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Education", "instances": 22, "metric_value": 0.8454, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Distance", "instances": 20, "metric_value": 0.8813, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					elif obj[2]>3:
						return 'True'
					else: return 'True'
				elif obj[4]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[3]<=4:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[1]<=0:
		# {"feature": "Restaurant20to50", "instances": 26, "metric_value": 0.7063, "depth": 2}
		if obj[4]>0.0:
			# {"feature": "Education", "instances": 18, "metric_value": 0.8524, "depth": 3}
			if obj[2]>0:
				# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						return 'True'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[2]<=0:
				# {"feature": "Distance", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[5]>2:
					# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[3]<=2:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]>0:
							return 'True'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					elif obj[3]>2:
						return 'False'
					else: return 'False'
				elif obj[5]<=2:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[4]<=0.0:
			return 'False'
		else: return 'False'
	else: return 'False'
