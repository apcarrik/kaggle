def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Education", "instances": 85, "metric_value": 0.9999, "depth": 1}
	if obj[4]<=2:
		# {"feature": "Age", "instances": 69, "metric_value": 0.9742, "depth": 2}
		if obj[3]>1:
			# {"feature": "Direction_same", "instances": 49, "metric_value": 0.9973, "depth": 3}
			if obj[9]<=0:
				# {"feature": "Occupation", "instances": 43, "metric_value": 0.9808, "depth": 4}
				if obj[5]<=11:
					# {"feature": "Time", "instances": 32, "metric_value": 0.9284, "depth": 5}
					if obj[1]>1:
						# {"feature": "Coffeehouse", "instances": 19, "metric_value": 0.7425, "depth": 6}
						if obj[7]>0.0:
							# {"feature": "Bar", "instances": 14, "metric_value": 0.8631, "depth": 7}
							if obj[6]<=1.0:
								# {"feature": "Coupon", "instances": 11, "metric_value": 0.9457, "depth": 8}
								if obj[2]>2:
									# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[10]>1:
										return 'True'
									elif obj[10]<=1:
										# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[0]<=3:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[8]<=1.0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[2]<=2:
									# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[8]<=1.0:
											# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[10]<=1:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[0]>1:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[6]>1.0:
								return 'True'
							else: return 'True'
						elif obj[7]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[1]<=1:
						# {"feature": "Bar", "instances": 13, "metric_value": 0.9957, "depth": 6}
						if obj[6]<=1.0:
							# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.994, "depth": 7}
							if obj[8]<=1.0:
								# {"feature": "Coupon", "instances": 8, "metric_value": 0.9544, "depth": 8}
								if obj[2]<=1:
									# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[10]<=2:
										# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[7]>0.0:
											return 'False'
										elif obj[7]<=0.0:
											return 'True'
										else: return 'True'
									elif obj[10]>2:
										return 'True'
									else: return 'True'
								elif obj[2]>1:
									return 'False'
								else: return 'False'
							elif obj[8]>1.0:
								return 'True'
							else: return 'True'
						elif obj[6]>1.0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[5]>11:
					# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[7]>0.0:
						# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[2]>0:
								return 'False'
							elif obj[2]<=0:
								return 'True'
							else: return 'True'
						elif obj[1]>2:
							return 'True'
						else: return 'True'
					elif obj[7]<=0.0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[9]>0:
				# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[6]<=2.0:
					return 'False'
				elif obj[6]>2.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]<=1:
			# {"feature": "Bar", "instances": 20, "metric_value": 0.8113, "depth": 3}
			if obj[6]<=1.0:
				# {"feature": "Occupation", "instances": 14, "metric_value": 0.9403, "depth": 4}
				if obj[5]<=20:
					# {"feature": "Coupon", "instances": 13, "metric_value": 0.8905, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Passanger", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[10]>1:
								# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[1]<=1:
									# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]>1.0:
										# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]<=1.0:
											return 'True'
										elif obj[8]>1.0:
											return 'False'
										else: return 'False'
									elif obj[7]<=1.0:
										return 'False'
									else: return 'False'
								elif obj[1]>1:
									return 'True'
								else: return 'True'
							elif obj[10]<=1:
								return 'True'
							else: return 'True'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					elif obj[2]>3:
						# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[7]<=1.0:
							return 'False'
						elif obj[7]>1.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[5]>20:
					return 'False'
				else: return 'False'
			elif obj[6]>1.0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[4]>2:
		# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.5436, "depth": 2}
		if obj[7]<=3.0:
			return 'False'
		elif obj[7]>3.0:
			# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[2]>1:
				# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[10]<=1:
					return 'True'
				elif obj[10]>1:
					return 'False'
				else: return 'False'
			elif obj[2]<=1:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
