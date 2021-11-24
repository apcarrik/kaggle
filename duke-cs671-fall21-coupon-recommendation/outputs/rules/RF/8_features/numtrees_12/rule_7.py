def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Restaurant20to50", "instances": 85, "metric_value": 0.9637, "depth": 1}
	if obj[5]<=2.0:
		# {"feature": "Occupation", "instances": 79, "metric_value": 0.9804, "depth": 2}
		if obj[3]<=20:
			# {"feature": "Coupon", "instances": 77, "metric_value": 0.9724, "depth": 3}
			if obj[1]>1:
				# {"feature": "Direction_same", "instances": 51, "metric_value": 0.9183, "depth": 4}
				if obj[6]<=0:
					# {"feature": "Bar", "instances": 38, "metric_value": 0.8315, "depth": 5}
					if obj[4]<=2.0:
						# {"feature": "Passanger", "instances": 36, "metric_value": 0.7642, "depth": 6}
						if obj[0]>0:
							# {"feature": "Education", "instances": 34, "metric_value": 0.7335, "depth": 7}
							if obj[2]<=2:
								# {"feature": "Distance", "instances": 28, "metric_value": 0.8113, "depth": 8}
								if obj[7]<=2:
									return 'True'
								elif obj[7]>2:
									return 'True'
								else: return 'True'
							elif obj[2]>2:
								return 'True'
							else: return 'True'
						elif obj[0]<=0:
							# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[2]<=0:
								return 'True'
							elif obj[2]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[4]>2.0:
						return 'False'
					else: return 'False'
				elif obj[6]>0:
					# {"feature": "Bar", "instances": 13, "metric_value": 0.9957, "depth": 5}
					if obj[4]<=2.0:
						# {"feature": "Passanger", "instances": 10, "metric_value": 0.8813, "depth": 6}
						if obj[0]>0:
							# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[2]>0:
								return 'False'
							elif obj[2]<=0:
								# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=1:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[0]<=0:
							# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2]>0:
								return 'True'
							elif obj[2]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[4]>2.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[1]<=1:
				# {"feature": "Education", "instances": 26, "metric_value": 0.9957, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Distance", "instances": 22, "metric_value": 0.9457, "depth": 5}
					if obj[7]>1:
						# {"feature": "Passanger", "instances": 13, "metric_value": 0.7793, "depth": 6}
						if obj[0]<=1:
							return 'False'
						elif obj[0]>1:
							# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[4]<=1.0:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							elif obj[4]>1.0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[7]<=1:
						# {"feature": "Bar", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[4]<=1.0:
							# {"feature": "Direction_same", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[0]<=0:
									return 'True'
								elif obj[0]>0:
									return 'False'
								else: return 'False'
							elif obj[6]>0:
								# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[0]<=1:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[4]>1.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[2]>3:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]>20:
			return 'False'
		else: return 'False'
	elif obj[5]>2.0:
		return 'True'
	else: return 'True'
