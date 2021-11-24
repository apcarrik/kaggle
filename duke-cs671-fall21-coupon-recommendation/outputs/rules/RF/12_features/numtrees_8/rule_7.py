def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9838, "depth": 1}
	if obj[2]>1:
		# {"feature": "Bar", "instances": 95, "metric_value": 0.9317, "depth": 2}
		if obj[7]<=3.0:
			# {"feature": "Education", "instances": 92, "metric_value": 0.9109, "depth": 3}
			if obj[5]<=2:
				# {"feature": "Distance", "instances": 70, "metric_value": 0.8224, "depth": 4}
				if obj[11]<=1:
					# {"feature": "Coffeehouse", "instances": 38, "metric_value": 0.6892, "depth": 5}
					if obj[8]>1.0:
						# {"feature": "Age", "instances": 20, "metric_value": 0.8813, "depth": 6}
						if obj[4]>2:
							# {"feature": "Occupation", "instances": 15, "metric_value": 0.7219, "depth": 7}
							if obj[6]>2:
								# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9183, "depth": 8}
								if obj[9]>0.0:
									# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[0]>0:
										# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[1]>0:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[3]>0:
												return 'False'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										elif obj[1]<=0:
											return 'True'
										else: return 'True'
									elif obj[0]<=0:
										return 'False'
									else: return 'False'
								elif obj[9]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[6]<=2:
								return 'True'
							else: return 'True'
						elif obj[4]<=2:
							# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[0]>1:
								return 'False'
							elif obj[0]<=1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[8]<=1.0:
						# {"feature": "Age", "instances": 18, "metric_value": 0.3095, "depth": 6}
						if obj[4]<=5:
							return 'True'
						elif obj[4]>5:
							# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3]>0:
								return 'False'
							elif obj[3]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[11]>1:
					# {"feature": "Coffeehouse", "instances": 32, "metric_value": 0.9284, "depth": 5}
					if obj[8]<=2.0:
						# {"feature": "Age", "instances": 26, "metric_value": 0.9829, "depth": 6}
						if obj[4]<=5:
							# {"feature": "Occupation", "instances": 22, "metric_value": 1.0, "depth": 7}
							if obj[6]>1:
								# {"feature": "Time", "instances": 19, "metric_value": 0.9819, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Passanger", "instances": 15, "metric_value": 0.9183, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Gender", "instances": 8, "metric_value": 1.0, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.9852, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[9]>1.0:
												return 'False'
											else: return 'False'
										elif obj[3]>0:
											return 'False'
										else: return 'False'
									elif obj[0]>1:
										# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.5917, "depth": 10}
										if obj[9]>0.0:
											return 'True'
										elif obj[9]<=0.0:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]>3:
									# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[0]>1:
										return 'False'
									elif obj[0]<=1:
										# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[9]<=0.0:
											return 'False'
										elif obj[9]>0.0:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'False'
							elif obj[6]<=1:
								return 'False'
							else: return 'False'
						elif obj[4]>5:
							return 'True'
						else: return 'True'
					elif obj[8]>2.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[5]>2:
				# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.994, "depth": 4}
				if obj[9]<=1.0:
					# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.9774, "depth": 5}
					if obj[8]<=2.0:
						# {"feature": "Age", "instances": 13, "metric_value": 0.9957, "depth": 6}
						if obj[4]<=1:
							# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[6]<=14:
								return 'True'
							elif obj[6]>14:
								# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[0]>1:
									# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[1]<=2:
										return 'True'
									elif obj[1]>2:
										return 'False'
									else: return 'False'
								elif obj[0]<=1:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[4]>1:
							# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[3]>0:
								return 'False'
							elif obj[3]<=0:
								# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=6:
									return 'True'
								elif obj[6]>6:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'False'
					elif obj[8]>2.0:
						return 'True'
					else: return 'True'
				elif obj[9]>1.0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[7]>3.0:
			return 'False'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Coffeehouse", "instances": 32, "metric_value": 0.9284, "depth": 2}
		if obj[8]<=2.0:
			# {"feature": "Restaurant20to50", "instances": 25, "metric_value": 0.9896, "depth": 3}
			if obj[9]>0.0:
				# {"feature": "Occupation", "instances": 21, "metric_value": 0.9984, "depth": 4}
				if obj[6]>5:
					# {"feature": "Age", "instances": 12, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=5:
						# {"feature": "Bar", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[7]<=1.0:
							return 'False'
						elif obj[7]>1.0:
							# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[0]>1:
								# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[1]>2:
									# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[11]>1:
										return 'False'
									elif obj[11]<=1:
										return 'True'
									else: return 'True'
								elif obj[1]<=2:
									return 'True'
								else: return 'True'
							elif obj[0]<=1:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[4]>5:
						return 'True'
					else: return 'True'
				elif obj[6]<=5:
					# {"feature": "Bar", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[7]>0.0:
						return 'True'
					elif obj[7]<=0.0:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=1:
							return 'False'
						elif obj[5]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[9]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[8]>2.0:
			return 'False'
		else: return 'False'
	else: return 'False'
