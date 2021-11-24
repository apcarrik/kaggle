def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[1]>1:
		# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.7642, "depth": 2}
		if obj[5]<=2.0:
			# {"feature": "Occupation", "instances": 17, "metric_value": 0.6723, "depth": 3}
			if obj[3]<=11:
				# {"feature": "Passanger", "instances": 13, "metric_value": 0.7793, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Education", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[2]<=2:
						return 'True'
					elif obj[2]>2:
						return 'False'
					else: return 'False'
				elif obj[0]>2:
					# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[7]>1:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=0:
							# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]<=2.0:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[2]>0:
							return 'False'
						else: return 'False'
					elif obj[7]<=1:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[3]>11:
				return 'True'
			else: return 'True'
		elif obj[5]>2.0:
			return 'False'
		else: return 'False'
	elif obj[1]<=1:
		return 'False'
	else: return 'False'
