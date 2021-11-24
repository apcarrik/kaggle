def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Occupation", "instances": 42, "metric_value": 0.9183, "depth": 2}
		if obj[3]<=18:
			# {"feature": "Coupon", "instances": 37, "metric_value": 0.9569, "depth": 3}
			if obj[1]>2:
				# {"feature": "Distance", "instances": 20, "metric_value": 1.0, "depth": 4}
				if obj[6]<=2:
					# {"feature": "Direction_same", "instances": 16, "metric_value": 0.9544, "depth": 5}
					if obj[5]<=0:
						# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.8905, "depth": 6}
						if obj[4]>0.0:
							# {"feature": "Education", "instances": 11, "metric_value": 0.8454, "depth": 7}
							if obj[2]>0:
								return 'False'
							elif obj[2]<=0:
								return 'False'
							else: return 'False'
						elif obj[4]<=0.0:
							# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[2]<=0:
								return 'True'
							elif obj[2]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[5]>0:
						# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]<=1.0:
							return 'True'
						elif obj[4]>1.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[6]>2:
					return 'True'
				else: return 'True'
			elif obj[1]<=2:
				# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.7871, "depth": 4}
				if obj[4]>1.0:
					# {"feature": "Education", "instances": 12, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[6]<=2:
							# {"feature": "Direction_same", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[6]>2:
							return 'False'
						else: return 'False'
					elif obj[2]>2:
						# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[6]<=2:
							return 'False'
						elif obj[6]>2:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[4]<=1.0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[3]>18:
			return 'False'
		else: return 'False'
	elif obj[0]>2:
		# {"feature": "Coupon", "instances": 9, "metric_value": 0.7642, "depth": 2}
		if obj[1]<=2:
			return 'True'
		elif obj[1]>2:
			# {"feature": "Occupation", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[3]<=2:
				return 'True'
			elif obj[3]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
