def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Direction_same", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[5]<=0:
		# {"feature": "Occupation", "instances": 19, "metric_value": 0.9819, "depth": 2}
		if obj[3]<=10:
			# {"feature": "Education", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[2]>0:
				# {"feature": "Coupon", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[1]>0:
					# {"feature": "Passanger", "instances": 8, "metric_value": 1.0, "depth": 5}
					if obj[0]>0:
						# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[4]>0.0:
							# {"feature": "Distance", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[6]<=2:
								return 'True'
							elif obj[6]>2:
								return 'False'
							else: return 'False'
						elif obj[4]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			elif obj[2]<=0:
				# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[1]<=2:
					return 'True'
				elif obj[1]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[3]>10:
			return 'False'
		else: return 'False'
	elif obj[5]>0:
		return 'True'
	else: return 'True'
