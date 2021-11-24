def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9879, "depth": 1}
	if obj[2]<=2:
		# {"feature": "Time", "instances": 44, "metric_value": 0.9624, "depth": 2}
		if obj[1]>0:
			# {"feature": "Education", "instances": 36, "metric_value": 0.888, "depth": 3}
			if obj[3]>0:
				# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.6666, "depth": 4}
				if obj[6]<=2.0:
					# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.3228, "depth": 5}
					if obj[7]<=2.0:
						return 'False'
					elif obj[7]>2.0:
						return 'True'
					else: return 'True'
				elif obj[6]>2.0:
					# {"feature": "Occupation", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[4]<=10:
						# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[0]>0:
							return 'False'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					elif obj[4]>10:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[3]<=0:
				# {"feature": "Passanger", "instances": 13, "metric_value": 0.9957, "depth": 4}
				if obj[0]>1:
					# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[4]<=12:
						# {"feature": "Bar", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[5]<=1.0:
							return 'True'
						elif obj[5]>1.0:
							# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=2.0:
								return 'False'
							elif obj[6]>2.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[4]>12:
						return 'False'
					else: return 'False'
				elif obj[0]<=1:
					# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[5]<=1.0:
						return 'False'
					elif obj[5]>1.0:
						# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]<=6:
							return 'True'
						elif obj[4]>6:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[1]<=0:
			# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[4]<=9:
				return 'True'
			elif obj[4]>9:
				# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[2]>2:
		# {"feature": "Passanger", "instances": 41, "metric_value": 0.8015, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Bar", "instances": 28, "metric_value": 0.9059, "depth": 3}
			if obj[5]<=2.0:
				# {"feature": "Coffeehouse", "instances": 24, "metric_value": 0.9544, "depth": 4}
				if obj[6]<=3.0:
					# {"feature": "Occupation", "instances": 23, "metric_value": 0.9321, "depth": 5}
					if obj[4]<=12:
						# {"feature": "Education", "instances": 21, "metric_value": 0.9587, "depth": 6}
						if obj[3]<=3:
							# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.9183, "depth": 7}
							if obj[7]>-1.0:
								# {"feature": "Time", "instances": 17, "metric_value": 0.9367, "depth": 8}
								if obj[1]<=1:
									# {"feature": "Distance", "instances": 13, "metric_value": 0.8905, "depth": 9}
									if obj[9]>1:
										# {"feature": "Direction_same", "instances": 8, "metric_value": 0.8113, "depth": 10}
										if obj[8]<=0:
											return 'True'
										elif obj[8]>0:
											return 'True'
										else: return 'True'
									elif obj[9]<=1:
										# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[8]<=1:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]>1:
									# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[9]<=1:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[9]>1:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[7]<=-1.0:
								return 'True'
							else: return 'True'
						elif obj[3]>3:
							# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[1]<=1:
								return 'False'
							elif obj[1]>1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[4]>12:
						return 'True'
					else: return 'True'
				elif obj[6]>3.0:
					return 'False'
				else: return 'False'
			elif obj[5]>2.0:
				return 'True'
			else: return 'True'
		elif obj[0]>2:
			# {"feature": "Bar", "instances": 13, "metric_value": 0.3912, "depth": 3}
			if obj[5]>0.0:
				return 'True'
			elif obj[5]<=0.0:
				# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[4]<=5:
					return 'True'
				elif obj[4]>5:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	else: return 'True'
