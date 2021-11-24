def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Passanger", "instances": 85, "metric_value": 0.9975, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Coupon", "instances": 60, "metric_value": 0.9871, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Restaurant20to50", "instances": 40, "metric_value": 1.0, "depth": 3}
			if obj[4]>0.0:
				# {"feature": "Occupation", "instances": 36, "metric_value": 0.9911, "depth": 4}
				if obj[3]<=12:
					# {"feature": "Education", "instances": 30, "metric_value": 1.0, "depth": 5}
					if obj[2]>0:
						# {"feature": "Direction_same", "instances": 21, "metric_value": 0.9852, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Distance", "instances": 18, "metric_value": 0.9911, "depth": 7}
							if obj[6]>1:
								return 'False'
							elif obj[6]<=1:
								return 'True'
							else: return 'True'
						elif obj[5]>0:
							# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=1:
								return 'False'
							elif obj[6]>1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[2]<=0:
						# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[6]<=2:
							# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]>2:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[3]>12:
					# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[6]>1:
						return 'False'
					elif obj[6]<=1:
						# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[2]<=1:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[4]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[1]>3:
			# {"feature": "Occupation", "instances": 20, "metric_value": 0.8813, "depth": 3}
			if obj[3]>4:
				# {"feature": "Education", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[4]>0.0:
						# {"feature": "Direction_same", "instances": 8, "metric_value": 1.0, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[6]<=1:
								return 'False'
							elif obj[6]>1:
								return 'False'
							else: return 'False'
						elif obj[5]>0:
							return 'True'
						else: return 'True'
					elif obj[4]<=0.0:
						# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]<=0:
							return 'True'
						elif obj[5]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[2]>3:
					return 'False'
				else: return 'False'
			elif obj[3]<=4:
				# {"feature": "Direction_same", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[5]<=0:
					return 'False'
				elif obj[5]>0:
					# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2]>1:
						return 'False'
					elif obj[2]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]>2:
		# {"feature": "Occupation", "instances": 25, "metric_value": 0.795, "depth": 2}
		if obj[3]>2:
			# {"feature": "Education", "instances": 19, "metric_value": 0.8997, "depth": 3}
			if obj[2]<=2:
				# {"feature": "Coupon", "instances": 15, "metric_value": 0.971, "depth": 4}
				if obj[1]>2:
					# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.8454, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[6]>1:
							# {"feature": "Direction_same", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]<=1:
							return 'True'
						else: return 'True'
					elif obj[4]>1.0:
						return 'True'
					else: return 'True'
				elif obj[1]<=2:
					# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[6]<=1:
						return 'False'
					elif obj[6]>1:
						# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]<=2.0:
							return 'True'
						elif obj[4]>2.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[2]>2:
				return 'True'
			else: return 'True'
		elif obj[3]<=2:
			return 'True'
		else: return 'True'
	else: return 'True'
