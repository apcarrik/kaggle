def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[2]>0:
		# {"feature": "Bar", "instances": 21, "metric_value": 0.9852, "depth": 2}
		if obj[5]>0.0:
			# {"feature": "Education", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[3]<=2:
				# {"feature": "Time", "instances": 10, "metric_value": 1.0, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[6]>0.0:
						# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[4]<=17:
							return 'False'
						elif obj[4]>17:
							# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[7]>1.0:
								return 'False'
							elif obj[7]<=1.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[6]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[1]>2:
					return 'True'
				else: return 'True'
			elif obj[3]>2:
				return 'False'
			else: return 'False'
		elif obj[5]<=0.0:
			# {"feature": "Education", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[3]>0:
				# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[1]<=0:
					return 'True'
				elif obj[1]>0:
					# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]<=10:
						return 'False'
					elif obj[4]>10:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[3]<=0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[2]<=0:
		return 'False'
	else: return 'False'
