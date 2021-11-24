def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Occupation", "instances": 85, "metric_value": 0.9999, "depth": 1}
	if obj[3]<=7:
		# {"feature": "Coupon", "instances": 46, "metric_value": 0.9503, "depth": 2}
		if obj[1]>0:
			# {"feature": "Passanger", "instances": 36, "metric_value": 0.7642, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Distance", "instances": 24, "metric_value": 0.8709, "depth": 4}
				if obj[6]<=1:
					# {"feature": "Education", "instances": 12, "metric_value": 0.65, "depth": 5}
					if obj[2]<=0:
						# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[4]>0.0:
							# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[4]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[2]>0:
						return 'True'
					else: return 'True'
				elif obj[6]>1:
					# {"feature": "Direction_same", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[5]<=0:
						# {"feature": "Education", "instances": 11, "metric_value": 0.9457, "depth": 6}
						if obj[2]>0:
							# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[4]>0.0:
								return 'True'
							elif obj[4]<=0.0:
								return 'True'
							else: return 'True'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					elif obj[5]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[0]>2:
				# {"feature": "Education", "instances": 12, "metric_value": 0.4138, "depth": 4}
				if obj[2]>0:
					return 'True'
				elif obj[2]<=0:
					# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[6]<=1:
							return 'False'
						elif obj[6]>1:
							return 'True'
						else: return 'True'
					elif obj[4]>1.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[1]<=0:
			# {"feature": "Education", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[2]>0:
				return 'False'
			elif obj[2]<=0:
				# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[4]<=0.0:
					return 'False'
				elif obj[4]>0.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[3]>7:
		# {"feature": "Restaurant20to50", "instances": 39, "metric_value": 0.9183, "depth": 2}
		if obj[4]<=2.0:
			# {"feature": "Education", "instances": 36, "metric_value": 0.8524, "depth": 3}
			if obj[2]>1:
				# {"feature": "Distance", "instances": 27, "metric_value": 0.6913, "depth": 4}
				if obj[6]<=2:
					# {"feature": "Coupon", "instances": 23, "metric_value": 0.7554, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Passanger", "instances": 13, "metric_value": 0.8905, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Direction_same", "instances": 11, "metric_value": 0.8454, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[1]>3:
						# {"feature": "Passanger", "instances": 10, "metric_value": 0.469, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Direction_same", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[6]>2:
					return 'False'
				else: return 'False'
			elif obj[2]<=1:
				# {"feature": "Coupon", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[5]<=0:
						return 'True'
					elif obj[5]>0:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=1:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[1]>2:
					# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[6]>1:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]<=3:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[6]<=1:
						return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[4]>2.0:
			return 'True'
		else: return 'True'
	else: return 'False'
