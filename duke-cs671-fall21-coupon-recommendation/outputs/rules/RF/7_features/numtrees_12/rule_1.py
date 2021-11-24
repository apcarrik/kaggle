def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Passanger", "instances": 85, "metric_value": 0.9975, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Education", "instances": 66, "metric_value": 0.9834, "depth": 2}
		if obj[2]<=2:
			# {"feature": "Occupation", "instances": 56, "metric_value": 0.9403, "depth": 3}
			if obj[3]<=5:
				# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.7973, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Coupon", "instances": 27, "metric_value": 0.7642, "depth": 5}
					if obj[1]<=2:
						# {"feature": "Direction_same", "instances": 16, "metric_value": 0.6962, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Distance", "instances": 14, "metric_value": 0.7496, "depth": 7}
							if obj[6]<=2:
								return 'False'
							elif obj[6]>2:
								return 'False'
							else: return 'False'
						elif obj[5]>0:
							return 'False'
						else: return 'False'
					elif obj[1]>2:
						# {"feature": "Direction_same", "instances": 11, "metric_value": 0.8454, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Distance", "instances": 9, "metric_value": 0.7642, "depth": 7}
							if obj[6]>1:
								return 'False'
							elif obj[6]<=1:
								return 'False'
							else: return 'False'
						elif obj[5]>0:
							# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=1:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[4]<=0.0:
					# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]<=0:
						return 'False'
					elif obj[1]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[3]>5:
				# {"feature": "Coupon", "instances": 27, "metric_value": 0.999, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Distance", "instances": 17, "metric_value": 0.9774, "depth": 5}
					if obj[6]<=1:
						# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.7642, "depth": 6}
						if obj[4]>0.0:
							# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5436, "depth": 7}
							if obj[5]>0:
								return 'True'
							elif obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[4]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[6]>1:
						# {"feature": "Direction_same", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[4]>1.0:
								return 'True'
							elif obj[4]<=1.0:
								return 'False'
							else: return 'False'
						elif obj[5]>0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[1]>3:
					# {"feature": "Distance", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[6]<=1:
						return 'False'
					elif obj[6]>1:
						# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[4]>0.0:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[4]<=0.0:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[2]>2:
			# {"feature": "Coupon", "instances": 10, "metric_value": 0.7219, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[6]>1:
					return 'True'
				elif obj[6]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Occupation", "instances": 19, "metric_value": 0.4855, "depth": 2}
		if obj[3]>3:
			return 'True'
		elif obj[3]<=3:
			# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[2]>0:
				# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[4]<=2.0:
					return 'True'
				elif obj[4]>2.0:
					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[6]>1:
						return 'True'
					elif obj[6]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
