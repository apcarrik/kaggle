def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Time", "instances": 85, "metric_value": 0.9975, "depth": 1}
	if obj[1]<=1:
		# {"feature": "Occupation", "instances": 45, "metric_value": 0.9389, "depth": 2}
		if obj[4]<=10:
			# {"feature": "Coupon", "instances": 33, "metric_value": 0.9834, "depth": 3}
			if obj[2]>1:
				# {"feature": "Bar", "instances": 19, "metric_value": 0.9819, "depth": 4}
				if obj[5]<=1.0:
					# {"feature": "Education", "instances": 13, "metric_value": 0.7793, "depth": 5}
					if obj[3]>1:
						# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=2.0:
								# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[7]>1.0:
									# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[9]<=2:
											return 'True'
										else: return 'True'
									elif obj[8]>0:
										return 'True'
									else: return 'True'
								elif obj[7]<=1.0:
									return 'True'
								else: return 'True'
							elif obj[6]>2.0:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					elif obj[3]<=1:
						return 'True'
					else: return 'True'
				elif obj[5]>1.0:
					# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[9]<=2:
						return 'False'
					elif obj[9]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[2]<=1:
				# {"feature": "Education", "instances": 14, "metric_value": 0.7496, "depth": 4}
				if obj[3]<=0:
					return 'False'
				elif obj[3]>0:
					# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[7]>1.0:
						# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[5]<=2.0:
							return 'False'
						elif obj[5]>2.0:
							return 'True'
						else: return 'True'
					elif obj[7]<=1.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[4]>10:
			# {"feature": "Coupon", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=1:
					# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[7]<=1.0:
						return 'True'
					elif obj[7]>1.0:
						return 'False'
					else: return 'False'
				elif obj[3]>1:
					return 'False'
				else: return 'False'
			elif obj[2]>3:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[1]>1:
		# {"feature": "Restaurant20to50", "instances": 40, "metric_value": 0.8485, "depth": 2}
		if obj[7]<=1.0:
			# {"feature": "Bar", "instances": 27, "metric_value": 0.9751, "depth": 3}
			if obj[5]<=0.0:
				# {"feature": "Coupon", "instances": 16, "metric_value": 0.8113, "depth": 4}
				if obj[2]>1:
					# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.5917, "depth": 5}
					if obj[6]<=1.0:
						return 'True'
					elif obj[6]>1.0:
						# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[3]<=2:
							# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[9]>1:
								return 'False'
							elif obj[9]<=1:
								return 'True'
							else: return 'True'
						elif obj[3]>2:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[2]<=1:
					return 'False'
				else: return 'False'
			elif obj[5]>0.0:
				# {"feature": "Occupation", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[4]<=7:
					# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[3]<=2:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[0]>1:
							# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2]<=0:
								# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=1.0:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[9]<=2:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[2]>0:
								return 'True'
							else: return 'True'
						elif obj[0]<=1:
							return 'False'
						else: return 'False'
					elif obj[3]>2:
						return 'True'
					else: return 'True'
				elif obj[4]>7:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[7]>1.0:
			return 'True'
		else: return 'True'
	else: return 'True'
