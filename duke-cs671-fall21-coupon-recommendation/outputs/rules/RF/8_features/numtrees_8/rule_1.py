def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9802, "depth": 1}
	if obj[1]>0:
		# {"feature": "Bar", "instances": 105, "metric_value": 0.9362, "depth": 2}
		if obj[4]<=2.0:
			# {"feature": "Education", "instances": 94, "metric_value": 0.8787, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Occupation", "instances": 86, "metric_value": 0.9103, "depth": 4}
				if obj[3]>0:
					# {"feature": "Restaurant20to50", "instances": 83, "metric_value": 0.9223, "depth": 5}
					if obj[5]<=1.0:
						# {"feature": "Direction_same", "instances": 47, "metric_value": 0.9734, "depth": 6}
						if obj[6]<=0:
							# {"feature": "Distance", "instances": 39, "metric_value": 0.9881, "depth": 7}
							if obj[7]>1:
								# {"feature": "Passanger", "instances": 28, "metric_value": 0.9666, "depth": 8}
								if obj[0]<=2:
									return 'True'
								elif obj[0]>2:
									return 'True'
								else: return 'True'
							elif obj[7]<=1:
								# {"feature": "Passanger", "instances": 11, "metric_value": 0.994, "depth": 8}
								if obj[0]>0:
									return 'False'
								elif obj[0]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[6]>0:
							# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[0]>0:
								# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[7]>1:
									return 'True'
								elif obj[7]<=1:
									return 'True'
								else: return 'True'
							elif obj[0]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[5]>1.0:
						# {"feature": "Passanger", "instances": 36, "metric_value": 0.8113, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Direction_same", "instances": 26, "metric_value": 0.8905, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Distance", "instances": 24, "metric_value": 0.9183, "depth": 8}
								if obj[7]<=2:
									return 'True'
								elif obj[7]>2:
									return 'True'
								else: return 'True'
							elif obj[6]>0:
								return 'True'
							else: return 'True'
						elif obj[0]>2:
							# {"feature": "Distance", "instances": 10, "metric_value": 0.469, "depth": 7}
							if obj[7]>1:
								# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[7]<=1:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[3]<=0:
					return 'True'
				else: return 'True'
			elif obj[2]>3:
				return 'True'
			else: return 'True'
		elif obj[4]>2.0:
			# {"feature": "Occupation", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[3]>6:
				return 'False'
			elif obj[3]<=6:
				# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[7]<=1:
					return 'True'
				elif obj[7]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[1]<=0:
		# {"feature": "Passanger", "instances": 22, "metric_value": 0.8454, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Bar", "instances": 20, "metric_value": 0.7219, "depth": 3}
			if obj[4]>0.0:
				# {"feature": "Distance", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[7]<=2:
					# {"feature": "Occupation", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[3]<=9:
						# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[5]<=2.0:
							# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[2]<=2:
								# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							elif obj[2]>2:
								return 'False'
							else: return 'False'
						elif obj[5]>2.0:
							return 'True'
						else: return 'True'
					elif obj[3]>9:
						return 'True'
					else: return 'True'
				elif obj[7]>2:
					return 'False'
				else: return 'False'
			elif obj[4]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[0]>2:
			return 'True'
		else: return 'True'
	else: return 'False'
