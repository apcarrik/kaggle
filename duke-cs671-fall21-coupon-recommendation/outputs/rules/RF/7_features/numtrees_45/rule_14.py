def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[3]>0:
		# {"feature": "Education", "instances": 21, "metric_value": 0.9183, "depth": 2}
		if obj[2]>0:
			# {"feature": "Coupon", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[4]<=1.0:
					# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[6]<=2:
								return 'False'
							elif obj[6]>2:
								return 'False'
							else: return 'False'
						elif obj[5]>0:
							return 'True'
						else: return 'True'
					elif obj[0]>2:
						return 'True'
					else: return 'True'
				elif obj[4]>1.0:
					return 'True'
				else: return 'True'
			elif obj[1]>3:
				# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[0]>0:
					return 'False'
				elif obj[0]<=0:
					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]>1.0:
						return 'False'
					elif obj[4]<=1.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[2]<=0:
			return 'True'
		else: return 'True'
	elif obj[3]<=0:
		return 'False'
	else: return 'False'
