def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Occupation", "instances": 19, "metric_value": 0.998, "depth": 2}
		if obj[4]>2:
			# {"feature": "Coupon", "instances": 15, "metric_value": 0.971, "depth": 3}
			if obj[2]>2:
				# {"feature": "Bar", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[5]<=2.0:
					# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[6]>-1.0:
							return 'False'
						elif obj[6]<=-1.0:
							return 'True'
						else: return 'True'
					elif obj[0]>2:
						return 'True'
					else: return 'True'
				elif obj[5]>2.0:
					return 'True'
				else: return 'True'
			elif obj[2]<=2:
				return 'True'
			else: return 'True'
		elif obj[4]<=2:
			return 'False'
		else: return 'False'
	elif obj[1]>2:
		return 'False'
	else: return 'False'
