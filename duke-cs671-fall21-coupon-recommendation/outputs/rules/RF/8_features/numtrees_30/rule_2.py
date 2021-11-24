def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Education", "instances": 22, "metric_value": 0.994, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Coupon", "instances": 20, "metric_value": 0.971, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Occupation", "instances": 17, "metric_value": 0.9975, "depth": 4}
				if obj[3]<=12:
					# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.971, "depth": 5}
					if obj[5]<=1.0:
						# {"feature": "Direction_same", "instances": 12, "metric_value": 0.9183, "depth": 6}
						if obj[6]<=0:
							# {"feature": "Bar", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[4]>-1.0:
								# {"feature": "Distance", "instances": 8, "metric_value": 1.0, "depth": 8}
								if obj[7]>1:
									return 'False'
								elif obj[7]<=1:
									return 'True'
								else: return 'True'
							elif obj[4]<=-1.0:
								return 'False'
							else: return 'False'
						elif obj[6]>0:
							return 'False'
						else: return 'False'
					elif obj[5]>1.0:
						# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]>-1.0:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]>0:
								return 'True'
							elif obj[6]<=0:
								return 'False'
							else: return 'False'
						elif obj[4]<=-1.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[3]>12:
					return 'True'
				else: return 'True'
			elif obj[1]>3:
				return 'False'
			else: return 'False'
		elif obj[2]>3:
			return 'True'
		else: return 'True'
	elif obj[0]>1:
		# {"feature": "Education", "instances": 12, "metric_value": 0.65, "depth": 2}
		if obj[2]<=2:
			return 'True'
		elif obj[2]>2:
			# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[3]<=12:
				return 'False'
			elif obj[3]>12:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
