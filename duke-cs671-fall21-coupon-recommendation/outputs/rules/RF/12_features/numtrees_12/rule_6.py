def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.971, "depth": 1}
	if obj[2]>0:
		# {"feature": "Distance", "instances": 72, "metric_value": 0.9038, "depth": 2}
		if obj[11]>1:
			# {"feature": "Bar", "instances": 41, "metric_value": 0.9789, "depth": 3}
			if obj[7]<=1.0:
				# {"feature": "Age", "instances": 25, "metric_value": 0.8555, "depth": 4}
				if obj[4]<=5:
					# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.5665, "depth": 5}
					if obj[8]>0.0:
						return 'True'
					elif obj[8]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[4]>5:
					# {"feature": "Time", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[1]>0:
						# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[8]<=0.0:
							# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[6]>0:
								return 'True'
							elif obj[6]<=0:
								return 'False'
							else: return 'False'
						elif obj[8]>0.0:
							return 'False'
						else: return 'False'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[7]>1.0:
				# {"feature": "Time", "instances": 16, "metric_value": 0.9544, "depth": 4}
				if obj[1]>0:
					# {"feature": "Age", "instances": 12, "metric_value": 1.0, "depth": 5}
					if obj[4]>0:
						# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[6]<=7:
							return 'True'
						elif obj[6]>7:
							# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[0]<=2:
								# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[5]<=0:
									# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]<=1.0:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[5]>0:
									return 'True'
								else: return 'True'
							elif obj[0]>2:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[4]<=0:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[11]<=1:
			# {"feature": "Restaurant20to50", "instances": 31, "metric_value": 0.7088, "depth": 3}
			if obj[9]<=1.0:
				# {"feature": "Passanger", "instances": 19, "metric_value": 0.8997, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Age", "instances": 14, "metric_value": 0.9852, "depth": 5}
					if obj[4]>0:
						# {"feature": "Bar", "instances": 11, "metric_value": 0.994, "depth": 6}
						if obj[7]<=0.0:
							# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[6]<=20:
								# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[3]>0:
									return 'True'
								elif obj[3]<=0:
									# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[1]>0:
										return 'True'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[6]>20:
								return 'False'
							else: return 'False'
						elif obj[7]>0.0:
							return 'False'
						else: return 'False'
					elif obj[4]<=0:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[9]>1.0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[2]<=0:
		# {"feature": "Time", "instances": 13, "metric_value": 0.6194, "depth": 2}
		if obj[1]<=1:
			return 'False'
		elif obj[1]>1:
			# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[5]<=0:
				return 'False'
			elif obj[5]>0:
				# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[4]<=4:
					return 'True'
				elif obj[4]>4:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	else: return 'False'
