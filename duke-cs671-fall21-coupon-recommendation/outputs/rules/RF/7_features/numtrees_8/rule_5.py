def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Passanger", "instances": 127, "metric_value": 0.9899, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Occupation", "instances": 98, "metric_value": 0.9997, "depth": 2}
		if obj[3]<=7.285714285714286:
			# {"feature": "Education", "instances": 66, "metric_value": 0.9834, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Restaurant20to50", "instances": 61, "metric_value": 0.9951, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Coupon", "instances": 57, "metric_value": 0.9819, "depth": 5}
					if obj[1]>0:
						# {"feature": "Distance", "instances": 43, "metric_value": 0.933, "depth": 6}
						if obj[6]>1:
							# {"feature": "Direction_same", "instances": 24, "metric_value": 0.995, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[6]<=1:
							# {"feature": "Direction_same", "instances": 19, "metric_value": 0.7425, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[1]<=0:
						# {"feature": "Direction_same", "instances": 14, "metric_value": 0.9403, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Distance", "instances": 13, "metric_value": 0.9612, "depth": 7}
							if obj[6]>1:
								return 'False'
							elif obj[6]<=1:
								return 'False'
							else: return 'False'
						elif obj[5]>0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[4]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[2]>3:
				return 'True'
			else: return 'True'
		elif obj[3]>7.285714285714286:
			# {"feature": "Distance", "instances": 32, "metric_value": 0.896, "depth": 3}
			if obj[6]<=2:
				# {"feature": "Coupon", "instances": 25, "metric_value": 0.971, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Education", "instances": 16, "metric_value": 0.9887, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.9183, "depth": 6}
						if obj[4]>0.0:
							# {"feature": "Direction_same", "instances": 11, "metric_value": 0.8454, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[4]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[2]>2:
						# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[5]<=0:
							return 'False'
						elif obj[5]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[1]>3:
					# {"feature": "Education", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[2]>1:
						# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[4]>0.0:
							# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[4]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[2]<=1:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[6]>2:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]>2:
		# {"feature": "Coupon", "instances": 29, "metric_value": 0.7355, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.4537, "depth": 3}
			if obj[4]<=1.0:
				# {"feature": "Occupation", "instances": 16, "metric_value": 0.5436, "depth": 4}
				if obj[3]<=10:
					# {"feature": "Education", "instances": 14, "metric_value": 0.3712, "depth": 5}
					if obj[2]<=0:
						# {"feature": "Distance", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[6]>1:
							# {"feature": "Direction_same", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]<=1:
							return 'True'
						else: return 'True'
					elif obj[2]>0:
						return 'True'
					else: return 'True'
				elif obj[3]>10:
					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[6]<=1:
						return 'False'
					elif obj[6]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]>1.0:
				return 'True'
			else: return 'True'
		elif obj[1]>3:
			# {"feature": "Education", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[2]<=2:
				# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[3]>0:
					# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[6]<=1:
						return 'False'
					elif obj[6]>1:
						# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]<=1.0:
							return 'True'
						elif obj[4]>1.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[3]<=0:
					return 'True'
				else: return 'True'
			elif obj[2]>2:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'True'
