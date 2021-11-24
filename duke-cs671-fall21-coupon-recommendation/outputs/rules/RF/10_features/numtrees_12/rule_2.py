def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Bar", "instances": 85, "metric_value": 0.9999, "depth": 1}
	if obj[5]>0.0:
		# {"feature": "Restaurant20to50", "instances": 45, "metric_value": 0.9389, "depth": 2}
		if obj[7]>0.0:
			# {"feature": "Education", "instances": 38, "metric_value": 0.9819, "depth": 3}
			if obj[3]>0:
				# {"feature": "Distance", "instances": 26, "metric_value": 0.9957, "depth": 4}
				if obj[9]<=2:
					# {"feature": "Passanger", "instances": 23, "metric_value": 0.9656, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Coupon", "instances": 15, "metric_value": 0.8366, "depth": 6}
						if obj[2]>2:
							# {"feature": "Occupation", "instances": 11, "metric_value": 0.9457, "depth": 7}
							if obj[4]<=12:
								# {"feature": "Direction_same", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[8]<=0:
									# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[1]<=1:
										# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[6]<=2.0:
											return 'False'
										elif obj[6]>2.0:
											return 'True'
										else: return 'True'
									elif obj[1]>1:
										return 'True'
									else: return 'True'
								elif obj[8]>0:
									return 'False'
								else: return 'False'
							elif obj[4]>12:
								return 'False'
							else: return 'False'
						elif obj[2]<=2:
							return 'False'
						else: return 'False'
					elif obj[0]>1:
						# {"feature": "Occupation", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[4]<=11:
							# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[1]>0:
								# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[6]<=2.0:
									# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[2]<=3:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[6]>2.0:
									return 'True'
								else: return 'True'
							elif obj[1]<=0:
								return 'False'
							else: return 'False'
						elif obj[4]>11:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[9]>2:
					return 'True'
				else: return 'True'
			elif obj[3]<=0:
				# {"feature": "Occupation", "instances": 12, "metric_value": 0.65, "depth": 4}
				if obj[4]<=6:
					return 'True'
				elif obj[4]>6:
					# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[6]<=1.0:
							return 'False'
						elif obj[6]>1.0:
							return 'True'
						else: return 'True'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[7]<=0.0:
			return 'True'
		else: return 'True'
	elif obj[5]<=0.0:
		# {"feature": "Coupon", "instances": 40, "metric_value": 0.9341, "depth": 2}
		if obj[2]>0:
			# {"feature": "Education", "instances": 33, "metric_value": 0.9834, "depth": 3}
			if obj[3]<=2:
				# {"feature": "Occupation", "instances": 22, "metric_value": 0.994, "depth": 4}
				if obj[4]>1:
					# {"feature": "Passanger", "instances": 20, "metric_value": 1.0, "depth": 5}
					if obj[0]>0:
						# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.998, "depth": 6}
						if obj[7]<=1.0:
							# {"feature": "Direction_same", "instances": 15, "metric_value": 0.971, "depth": 7}
							if obj[8]<=0:
								# {"feature": "Distance", "instances": 11, "metric_value": 0.8454, "depth": 8}
								if obj[9]<=1:
									# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[1]<=3:
										return 'False'
									elif obj[1]>3:
										# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6]<=1.0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[9]>1:
									# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[6]>0.0:
										# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[1]>0:
											return 'False'
										elif obj[1]<=0:
											return 'False'
										else: return 'False'
									elif obj[6]<=0.0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[8]>0:
								# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[1]<=1:
										# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[9]<=1:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[6]>0.0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[7]>1.0:
							# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[9]>1:
								# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[1]<=4:
									# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[6]<=2.0:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[9]<=1:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				elif obj[4]<=1:
					return 'True'
				else: return 'True'
			elif obj[3]>2:
				# {"feature": "Occupation", "instances": 11, "metric_value": 0.684, "depth": 4}
				if obj[4]<=7:
					return 'False'
				elif obj[4]>7:
					# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[6]>0.0:
						return 'True'
					elif obj[6]<=0.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	else: return 'False'
