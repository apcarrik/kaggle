def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9978, "depth": 1}
	if obj[2]>1:
		# {"feature": "Occupation", "instances": 90, "metric_value": 0.9825, "depth": 2}
		if obj[5]<=7.7:
			# {"feature": "Distance", "instances": 57, "metric_value": 0.9183, "depth": 3}
			if obj[10]>1:
				# {"feature": "Direction_same", "instances": 30, "metric_value": 0.9871, "depth": 4}
				if obj[9]<=0:
					# {"feature": "Age", "instances": 27, "metric_value": 0.951, "depth": 5}
					if obj[3]>1:
						# {"feature": "Coffeehouse", "instances": 19, "metric_value": 0.998, "depth": 6}
						if obj[7]<=3.0:
							# {"feature": "Bar", "instances": 15, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=3.0:
								# {"feature": "Time", "instances": 14, "metric_value": 0.8631, "depth": 8}
								if obj[1]>0:
									# {"feature": "Education", "instances": 12, "metric_value": 0.9183, "depth": 9}
									if obj[4]<=2:
										# {"feature": "Passanger", "instances": 11, "metric_value": 0.9457, "depth": 10}
										if obj[0]<=2:
											# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 1.0, "depth": 11}
											if obj[8]>0.0:
												return 'True'
											elif obj[8]<=0.0:
												return 'False'
											else: return 'False'
										elif obj[0]>2:
											# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[8]>1.0:
												return 'True'
											elif obj[8]<=1.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]>2:
										return 'True'
									else: return 'True'
								elif obj[1]<=0:
									return 'True'
								else: return 'True'
							elif obj[6]>3.0:
								return 'False'
							else: return 'False'
						elif obj[7]>3.0:
							return 'False'
						else: return 'False'
					elif obj[3]<=1:
						# {"feature": "Time", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[1]>1:
							return 'True'
						elif obj[1]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[9]>0:
					return 'False'
				else: return 'False'
			elif obj[10]<=1:
				# {"feature": "Bar", "instances": 27, "metric_value": 0.7642, "depth": 4}
				if obj[6]<=3.0:
					# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.5586, "depth": 5}
					if obj[7]>1.0:
						return 'True'
					elif obj[7]<=1.0:
						# {"feature": "Time", "instances": 10, "metric_value": 0.8813, "depth": 6}
						if obj[1]>1:
							# {"feature": "Age", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[3]>0:
								# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[8]>0.0:
									# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[0]<=0:
										# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[4]<=0:
											return 'True'
										elif obj[4]>0:
											return 'False'
										else: return 'False'
									elif obj[0]>0:
										return 'False'
									else: return 'False'
								elif obj[8]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[3]<=0:
								return 'True'
							else: return 'True'
						elif obj[1]<=1:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[6]>3.0:
					# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[1]<=1:
						return 'False'
					elif obj[1]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[5]>7.7:
			# {"feature": "Restaurant20to50", "instances": 33, "metric_value": 0.9834, "depth": 3}
			if obj[8]<=3.0:
				# {"feature": "Distance", "instances": 31, "metric_value": 0.9629, "depth": 4}
				if obj[10]>1:
					# {"feature": "Education", "instances": 17, "metric_value": 0.9975, "depth": 5}
					if obj[4]>0:
						# {"feature": "Age", "instances": 10, "metric_value": 0.8813, "depth": 6}
						if obj[3]>0:
							# {"feature": "Passanger", "instances": 8, "metric_value": 0.5436, "depth": 7}
							if obj[0]>0:
								return 'False'
							elif obj[0]<=0:
								return 'True'
							else: return 'True'
						elif obj[3]<=0:
							return 'True'
						else: return 'True'
					elif obj[4]<=0:
						# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[0]>0:
							return 'True'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[10]<=1:
					# {"feature": "Age", "instances": 14, "metric_value": 0.7496, "depth": 5}
					if obj[3]>2:
						# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[4]>0:
								# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[6]<=1.0:
									return 'True'
								elif obj[6]>1.0:
									return 'False'
								else: return 'False'
							elif obj[4]<=0:
								return 'False'
							else: return 'False'
						elif obj[1]>1:
							return 'False'
						else: return 'False'
					elif obj[3]<=2:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[8]>3.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Bar", "instances": 37, "metric_value": 0.974, "depth": 2}
		if obj[6]>0.0:
			# {"feature": "Time", "instances": 26, "metric_value": 0.9957, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Coffeehouse", "instances": 22, "metric_value": 0.994, "depth": 4}
				if obj[7]>0.0:
					# {"feature": "Direction_same", "instances": 19, "metric_value": 0.9495, "depth": 5}
					if obj[9]<=0:
						# {"feature": "Education", "instances": 15, "metric_value": 0.8366, "depth": 6}
						if obj[4]<=3:
							# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.7496, "depth": 7}
							if obj[8]>-1.0:
								# {"feature": "Occupation", "instances": 13, "metric_value": 0.6194, "depth": 8}
								if obj[5]<=6:
									# {"feature": "Age", "instances": 7, "metric_value": 0.8631, "depth": 9}
									if obj[3]<=4:
										# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[0]>0:
											# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[10]<=2:
												return 'True'
											else: return 'True'
										elif obj[0]<=0:
											return 'False'
										else: return 'False'
									elif obj[3]>4:
										return 'False'
									else: return 'False'
								elif obj[5]>6:
									return 'False'
								else: return 'False'
							elif obj[8]<=-1.0:
								return 'True'
							else: return 'True'
						elif obj[4]>3:
							return 'True'
						else: return 'True'
					elif obj[9]>0:
						# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[5]>6:
							return 'True'
						elif obj[5]<=6:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[7]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[6]<=0.0:
			# {"feature": "Occupation", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[5]<=6:
				return 'False'
			elif obj[5]>6:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
