def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Passanger", "instances": 85, "metric_value": 0.9465, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Direction_same", "instances": 53, "metric_value": 0.9977, "depth": 2}
		if obj[9]<=0:
			# {"feature": "Occupation", "instances": 40, "metric_value": 0.9837, "depth": 3}
			if obj[5]>2:
				# {"feature": "Time", "instances": 28, "metric_value": 0.9059, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Age", "instances": 22, "metric_value": 0.976, "depth": 5}
					if obj[3]<=6:
						# {"feature": "Coupon", "instances": 19, "metric_value": 0.998, "depth": 6}
						if obj[2]<=3:
							# {"feature": "Bar", "instances": 11, "metric_value": 0.9457, "depth": 7}
							if obj[6]>0.0:
								# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[7]>0.0:
									# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[4]<=3:
										return 'False'
									elif obj[4]>3:
										return 'True'
									else: return 'True'
								elif obj[7]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[6]<=0.0:
								return 'True'
							else: return 'True'
						elif obj[2]>3:
							# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[8]>1.0:
								# {"feature": "Bar", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0.0:
									# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[4]<=0:
										# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[7]<=2.0:
											# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[10]<=3:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]>0:
										return 'False'
									else: return 'False'
								elif obj[6]>0.0:
									return 'True'
								else: return 'True'
							elif obj[8]<=1.0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[3]>6:
						return 'False'
					else: return 'False'
				elif obj[1]>2:
					return 'False'
				else: return 'False'
			elif obj[5]<=2:
				# {"feature": "Bar", "instances": 12, "metric_value": 0.9183, "depth": 4}
				if obj[6]<=1.0:
					# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[2]>1:
						# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[4]<=1:
							return 'True'
						elif obj[4]>1:
							return 'False'
						else: return 'False'
					elif obj[2]<=1:
						return 'False'
					else: return 'False'
				elif obj[6]>1.0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[9]>0:
			# {"feature": "Bar", "instances": 13, "metric_value": 0.6194, "depth": 3}
			if obj[6]<=1.0:
				return 'True'
			elif obj[6]>1.0:
				# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=1:
					return 'False'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[0]>1:
		# {"feature": "Coffeehouse", "instances": 32, "metric_value": 0.6962, "depth": 2}
		if obj[7]>0.0:
			# {"feature": "Coupon", "instances": 23, "metric_value": 0.4262, "depth": 3}
			if obj[2]>0:
				# {"feature": "Occupation", "instances": 22, "metric_value": 0.2668, "depth": 4}
				if obj[5]<=15:
					return 'True'
				elif obj[5]>15:
					# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[6]<=0.0:
						return 'True'
					elif obj[6]>0.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		elif obj[7]<=0.0:
			# {"feature": "Time", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[1]>0:
				# {"feature": "Occupation", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[5]>2:
					# {"feature": "Age", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[3]>2:
						# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[4]<=1:
							return 'True'
						elif obj[4]>1:
							return 'False'
						else: return 'False'
					elif obj[3]<=2:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]<=1:
							return 'False'
						elif obj[4]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[5]<=2:
					return 'True'
				else: return 'True'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'True'