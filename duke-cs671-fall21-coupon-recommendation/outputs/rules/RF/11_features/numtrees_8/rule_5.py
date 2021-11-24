def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9762, "depth": 1}
	if obj[2]>0:
		# {"feature": "Passanger", "instances": 106, "metric_value": 0.9245, "depth": 2}
		if obj[0]>0:
			# {"feature": "Occupation", "instances": 98, "metric_value": 0.9486, "depth": 3}
			if obj[5]>4:
				# {"feature": "Bar", "instances": 68, "metric_value": 0.874, "depth": 4}
				if obj[6]<=1.0:
					# {"feature": "Coffeehouse", "instances": 46, "metric_value": 0.7131, "depth": 5}
					if obj[7]<=2.0:
						# {"feature": "Age", "instances": 36, "metric_value": 0.8113, "depth": 6}
						if obj[3]>1:
							# {"feature": "Education", "instances": 19, "metric_value": 0.9495, "depth": 7}
							if obj[4]<=3:
								# {"feature": "Time", "instances": 17, "metric_value": 0.874, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.9403, "depth": 9}
									if obj[8]>0.0:
										# {"feature": "Distance", "instances": 13, "metric_value": 0.8905, "depth": 10}
										if obj[10]>1:
											# {"feature": "Direction_same", "instances": 10, "metric_value": 0.8813, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[10]<=1:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[8]<=0.0:
										return 'False'
									else: return 'False'
								elif obj[1]>3:
									return 'True'
								else: return 'True'
							elif obj[4]>3:
								return 'False'
							else: return 'False'
						elif obj[3]<=1:
							# {"feature": "Distance", "instances": 17, "metric_value": 0.5226, "depth": 7}
							if obj[10]>1:
								# {"feature": "Time", "instances": 10, "metric_value": 0.7219, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Direction_same", "instances": 9, "metric_value": 0.5033, "depth": 9}
									if obj[9]<=0:
										return 'True'
									elif obj[9]>0:
										# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[4]<=2:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[8]<=2.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]>3:
									return 'False'
								else: return 'False'
							elif obj[10]<=1:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[7]>2.0:
						return 'True'
					else: return 'True'
				elif obj[6]>1.0:
					# {"feature": "Education", "instances": 22, "metric_value": 1.0, "depth": 5}
					if obj[4]<=2:
						# {"feature": "Distance", "instances": 20, "metric_value": 0.9928, "depth": 6}
						if obj[10]<=2:
							# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.9641, "depth": 7}
							if obj[7]<=2.0:
								# {"feature": "Age", "instances": 13, "metric_value": 0.9957, "depth": 8}
								if obj[3]>0:
									# {"feature": "Direction_same", "instances": 12, "metric_value": 0.9799, "depth": 9}
									if obj[9]<=0:
										# {"feature": "Time", "instances": 11, "metric_value": 0.9457, "depth": 10}
										if obj[1]<=3:
											# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.971, "depth": 11}
											if obj[8]<=2.0:
												return 'False'
											elif obj[8]>2.0:
												return 'False'
											else: return 'False'
										elif obj[1]>3:
											return 'False'
										else: return 'False'
									elif obj[9]>0:
										return 'True'
									else: return 'True'
								elif obj[3]<=0:
									return 'True'
								else: return 'True'
							elif obj[7]>2.0:
								return 'True'
							else: return 'True'
						elif obj[10]>2:
							return 'False'
						else: return 'False'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[5]<=4:
				# {"feature": "Age", "instances": 30, "metric_value": 0.9968, "depth": 4}
				if obj[3]<=4:
					# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9877, "depth": 5}
					if obj[8]<=1.0:
						# {"feature": "Bar", "instances": 17, "metric_value": 0.9975, "depth": 6}
						if obj[6]<=1.0:
							# {"feature": "Time", "instances": 12, "metric_value": 0.9799, "depth": 7}
							if obj[1]<=3:
								# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 8}
								if obj[4]<=2:
									# {"feature": "Coffeehouse", "instances": 8, "metric_value": 1.0, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 10}
										if obj[9]<=0:
											# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[10]<=2:
												return 'False'
											elif obj[10]>2:
												return 'True'
											else: return 'True'
										elif obj[9]>0:
											return 'True'
										else: return 'True'
									elif obj[7]<=0.0:
										return 'True'
									else: return 'True'
								elif obj[4]>2:
									return 'False'
								else: return 'False'
							elif obj[1]>3:
								return 'True'
							else: return 'True'
						elif obj[6]>1.0:
							# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[7]<=3.0:
								return 'False'
							elif obj[7]>3.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[8]>1.0:
						# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[1]>0:
							return 'True'
						elif obj[1]<=0:
							# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]>2:
								return 'False'
							elif obj[4]<=2:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[3]>4:
					# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[1]<=3:
						return 'False'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	elif obj[2]<=0:
		# {"feature": "Education", "instances": 21, "metric_value": 0.7919, "depth": 2}
		if obj[4]>0:
			return 'False'
		elif obj[4]<=0:
			# {"feature": "Distance", "instances": 10, "metric_value": 1.0, "depth": 3}
			if obj[10]<=2:
				# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[5]>2:
					return 'True'
				elif obj[5]<=2:
					return 'False'
				else: return 'False'
			elif obj[10]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
