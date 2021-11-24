def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[8]<=2:
		# {"feature": "Education", "instances": 19, "metric_value": 0.9495, "depth": 2}
		if obj[3]<=1:
			# {"feature": "Occupation", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[4]<=12:
				# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[1]>0:
					# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[2]>3:
						return 'False'
					elif obj[2]<=3:
						# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[6]<=1.0:
							return 'False'
						elif obj[6]>1.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			elif obj[4]>12:
				return 'True'
			else: return 'True'
		elif obj[3]>1:
			# {"feature": "Time", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[8]>2:
		return 'False'
	else: return 'False'
