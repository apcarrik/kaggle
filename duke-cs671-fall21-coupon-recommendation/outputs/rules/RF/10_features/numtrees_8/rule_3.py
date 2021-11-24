def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9989, "depth": 1}
	if obj[2]>1:
		# {"feature": "Occupation", "instances": 91, "metric_value": 0.9957, "depth": 2}
		if obj[4]>5:
			# {"feature": "Bar", "instances": 54, "metric_value": 0.9911, "depth": 3}
			if obj[5]>0.0:
				# {"feature": "Passanger", "instances": 32, "metric_value": 0.896, "depth": 4}
				if obj[0]>0:
					# {"feature": "Coffeehouse", "instances": 31, "metric_value": 0.8691, "depth": 5}
					if obj[6]<=3.0:
						# {"feature": "Education", "instances": 28, "metric_value": 0.9059, "depth": 6}
						if obj[3]<=3:
							# {"feature": "Restaurant20to50", "instances": 26, "metric_value": 0.9306, "depth": 7}
							if obj[7]>-1.0:
								# {"feature": "Distance", "instances": 25, "metric_value": 0.9427, "depth": 8}
								if obj[9]<=2:
									# {"feature": "Direction_same", "instances": 20, "metric_value": 0.971, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Time", "instances": 16, "metric_value": 0.9544, "depth": 10}
										if obj[1]>1:
											return 'False'
										elif obj[1]<=1:
											return 'False'
										else: return 'False'
									elif obj[8]>0:
										# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[1]<=1:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[9]>2:
									# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[1]<=1:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[1]>1:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[7]<=-1.0:
								return 'False'
							else: return 'False'
						elif obj[3]>3:
							return 'False'
						else: return 'False'
					elif obj[6]>3.0:
						return 'False'
					else: return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			elif obj[5]<=0.0:
				# {"feature": "Education", "instances": 22, "metric_value": 0.9457, "depth": 4}
				if obj[3]<=2:
					# {"feature": "Direction_same", "instances": 17, "metric_value": 0.9975, "depth": 5}
					if obj[8]<=0:
						# {"feature": "Passanger", "instances": 15, "metric_value": 0.971, "depth": 6}
						if obj[0]>1:
							# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[1]>2:
								# {"feature": "Distance", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[9]>1:
									# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[6]>0.0:
										# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[7]>0.0:
											return 'True'
										elif obj[7]<=0.0:
											return 'False'
										else: return 'False'
									elif obj[6]<=0.0:
										return 'False'
									else: return 'False'
								elif obj[9]<=1:
									return 'True'
								else: return 'True'
							elif obj[1]<=2:
								return 'False'
							else: return 'False'
						elif obj[0]<=1:
							# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[1]>0:
								return 'True'
							elif obj[1]<=0:
								# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]>1.0:
									return 'True'
								elif obj[7]<=1.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[8]>0:
						return 'False'
					else: return 'False'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[4]<=5:
			# {"feature": "Time", "instances": 37, "metric_value": 0.909, "depth": 3}
			if obj[1]>1:
				# {"feature": "Bar", "instances": 20, "metric_value": 0.6098, "depth": 4}
				if obj[5]<=0.0:
					# {"feature": "Distance", "instances": 11, "metric_value": 0.8454, "depth": 5}
					if obj[9]>1:
						# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[0]>2:
							# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[7]>0.0:
								# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[6]<=0.0:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[7]<=0.0:
								return 'True'
							else: return 'True'
						elif obj[0]<=2:
							return 'False'
						else: return 'False'
					elif obj[9]<=1:
						return 'True'
					else: return 'True'
				elif obj[5]>0.0:
					return 'True'
				else: return 'True'
			elif obj[1]<=1:
				# {"feature": "Distance", "instances": 17, "metric_value": 0.9975, "depth": 4}
				if obj[9]<=2:
					# {"feature": "Passanger", "instances": 14, "metric_value": 0.9403, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Bar", "instances": 12, "metric_value": 0.9799, "depth": 6}
						if obj[5]<=3.0:
							# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.994, "depth": 7}
							if obj[7]<=2.0:
								# {"feature": "Direction_same", "instances": 9, "metric_value": 0.9183, "depth": 8}
								if obj[8]>0:
									# {"feature": "Coffeehouse", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[6]<=2.0:
										# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[3]>0:
											return 'True'
										elif obj[3]<=0:
											return 'False'
										else: return 'False'
									elif obj[6]>2.0:
										return 'False'
									else: return 'False'
								elif obj[8]<=0:
									return 'False'
								else: return 'False'
							elif obj[7]>2.0:
								return 'True'
							else: return 'True'
						elif obj[5]>3.0:
							return 'False'
						else: return 'False'
					elif obj[0]>2:
						return 'False'
					else: return 'False'
				elif obj[9]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Passanger", "instances": 36, "metric_value": 0.9183, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Bar", "instances": 23, "metric_value": 0.6666, "depth": 3}
			if obj[5]<=0.0:
				return 'False'
			elif obj[5]>0.0:
				# {"feature": "Time", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[1]>0:
					# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[4]>0:
						return 'False'
					elif obj[4]<=0:
						return 'True'
					else: return 'True'
				elif obj[1]<=0:
					# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[3]<=0:
						# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]>5:
							return 'False'
						elif obj[4]<=5:
							return 'True'
						else: return 'True'
					elif obj[3]>0:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[0]>1:
			# {"feature": "Occupation", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[4]<=6:
				# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[6]<=1.0:
					return 'False'
				elif obj[6]>1.0:
					return 'True'
				else: return 'True'
			elif obj[4]>6:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
