def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[4]<=10:
		# {"feature": "Education", "instances": 17, "metric_value": 0.9367, "depth": 2}
		if obj[3]>1:
			# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[7]<=1.0:
				# {"feature": "Coupon", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[2]>1:
					# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[5]>0.0:
						# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=0.0:
								return 'False'
							elif obj[6]>0.0:
								return 'True'
							else: return 'True'
						elif obj[1]>1:
							return 'True'
						else: return 'True'
					elif obj[5]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[2]<=1:
					return 'False'
				else: return 'False'
			elif obj[7]>1.0:
				# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[3]<=1:
			return 'True'
		else: return 'True'
	elif obj[4]>10:
		# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[2]>0:
			return 'False'
		elif obj[2]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
