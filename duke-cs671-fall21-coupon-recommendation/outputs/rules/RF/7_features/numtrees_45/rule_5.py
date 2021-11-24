def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[2]<=3:
		# {"feature": "Coupon", "instances": 18, "metric_value": 0.9911, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[4]>0.0:
				# {"feature": "Occupation", "instances": 10, "metric_value": 1.0, "depth": 4}
				if obj[3]>0:
					# {"feature": "Distance", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[6]<=2:
						# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[0]>0:
							# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					elif obj[6]>2:
						return 'False'
					else: return 'False'
				elif obj[3]<=0:
					return 'True'
				else: return 'True'
			elif obj[4]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[1]>3:
			return 'False'
		else: return 'False'
	elif obj[2]>3:
		return 'True'
	else: return 'True'
