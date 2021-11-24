def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9802, "depth": 1}
	if obj[2]>1:
		# {"feature": "Bar", "instances": 91, "metric_value": 0.9254, "depth": 2}
		if obj[9]>-1.0:
			# {"feature": "Education", "instances": 89, "metric_value": 0.9106, "depth": 3}
			if obj[6]<=2:
				# {"feature": "Age", "instances": 75, "metric_value": 0.8555, "depth": 4}
				if obj[4]>0:
					# {"feature": "Occupation", "instances": 64, "metric_value": 0.7579, "depth": 5}
					if obj[7]>2:
						# {"feature": "Coffeehouse", "instances": 53, "metric_value": 0.8329, "depth": 6}
						if obj[10]>0.0:
							# {"feature": "Passanger", "instances": 37, "metric_value": 0.6998, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Gender", "instances": 22, "metric_value": 0.9024, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Distance", "instances": 14, "metric_value": 0.5917, "depth": 9}
									if obj[13]<=2:
										return 'True'
									elif obj[13]>2:
										# {"feature": "Income", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[8]>0:
											# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[11]>0.0:
												return 'False'
											elif obj[11]<=0.0:
												return 'True'
											else: return 'True'
										elif obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[3]>0:
									# {"feature": "Income", "instances": 8, "metric_value": 0.9544, "depth": 9}
									if obj[8]>0:
										# {"feature": "Children", "instances": 7, "metric_value": 0.8631, "depth": 10}
										if obj[5]>0:
											# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 11}
											if obj[1]<=1:
												# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[13]<=1:
													return 'True'
												elif obj[13]>1:
													return 'False'
												else: return 'False'
											elif obj[1]>1:
												return 'False'
											else: return 'False'
										elif obj[5]<=0:
											return 'False'
										else: return 'False'
									elif obj[8]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						elif obj[10]<=0.0:
							# {"feature": "Time", "instances": 16, "metric_value": 0.9887, "depth": 7}
							if obj[1]<=2:
								# {"feature": "Passanger", "instances": 12, "metric_value": 0.9183, "depth": 8}
								if obj[0]>0:
									# {"feature": "Income", "instances": 11, "metric_value": 0.8454, "depth": 9}
									if obj[8]<=5:
										# {"feature": "Children", "instances": 7, "metric_value": 0.5917, "depth": 10}
										if obj[5]<=0:
											return 'True'
										elif obj[5]>0:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[3]>0:
												return 'True'
											elif obj[3]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[8]>5:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[12]<=0:
											# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[13]<=2:
												return 'True'
											elif obj[13]>2:
												return 'False'
											else: return 'False'
										elif obj[12]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[0]<=0:
									return 'False'
								else: return 'False'
							elif obj[1]>2:
								# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[0]>0:
									return 'False'
								elif obj[0]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					elif obj[7]<=2:
						return 'True'
					else: return 'True'
				elif obj[4]<=0:
					# {"feature": "Time", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[1]>1:
						# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[8]<=3:
								return 'False'
							elif obj[8]>3:
								return 'True'
							else: return 'True'
						elif obj[0]>2:
							return 'True'
						else: return 'True'
					elif obj[1]<=1:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[6]>2:
				# {"feature": "Age", "instances": 14, "metric_value": 0.9852, "depth": 4}
				if obj[4]>0:
					# {"feature": "Time", "instances": 11, "metric_value": 0.8454, "depth": 5}
					if obj[1]>1:
						return 'False'
					elif obj[1]<=1:
						# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[10]>1.0:
							return 'True'
						elif obj[10]<=1.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[4]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[9]<=-1.0:
			return 'False'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Occupation", "instances": 36, "metric_value": 0.9641, "depth": 2}
		if obj[7]>1:
			# {"feature": "Passanger", "instances": 33, "metric_value": 0.9183, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Education", "instances": 26, "metric_value": 0.7793, "depth": 4}
				if obj[6]<=2:
					# {"feature": "Income", "instances": 21, "metric_value": 0.8631, "depth": 5}
					if obj[8]>2:
						# {"feature": "Time", "instances": 17, "metric_value": 0.9367, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Age", "instances": 10, "metric_value": 1.0, "depth": 7}
							if obj[4]<=2:
								# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[10]>1.0:
									return 'True'
								elif obj[10]<=1.0:
									return 'False'
								else: return 'False'
							elif obj[4]>2:
								# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[10]>0.0:
									return 'False'
								elif obj[10]<=0.0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[1]>1:
							# {"feature": "Gender", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[3]<=0:
								return 'False'
							elif obj[3]>0:
								# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[4]<=0:
									return 'False'
								elif obj[4]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'False'
					elif obj[8]<=2:
						return 'False'
					else: return 'False'
				elif obj[6]>2:
					return 'False'
				else: return 'False'
			elif obj[0]>1:
				# {"feature": "Time", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[1]>2:
					return 'True'
				elif obj[1]<=2:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[6]>0:
						return 'False'
					elif obj[6]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[7]<=1:
			return 'True'
		else: return 'True'
	else: return 'False'
