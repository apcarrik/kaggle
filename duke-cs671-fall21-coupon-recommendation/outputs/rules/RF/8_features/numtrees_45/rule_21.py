def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Occupation", "instances": 19, "metric_value": 0.8997, "depth": 2}
		if obj[3]<=7:
			# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[5]<=1.0:
				# {"feature": "Distance", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[7]<=2:
					# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[1]<=0:
						return 'False'
					elif obj[1]>0:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]>0:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=0:
								return 'True'
							elif obj[6]>0:
								return 'False'
							else: return 'False'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[7]>2:
					return 'True'
				else: return 'True'
			elif obj[5]>1.0:
				# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[2]<=0:
					return 'True'
				elif obj[2]>0:
					# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]>2:
						return 'True'
					elif obj[1]<=2:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[3]>7:
			return 'False'
		else: return 'False'
	elif obj[0]>2:
		return 'True'
	else: return 'True'
