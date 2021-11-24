def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[3]<=4:
		# {"feature": "Occupation", "instances": 20, "metric_value": 0.9928, "depth": 2}
		if obj[5]<=7:
			# {"feature": "Passanger", "instances": 15, "metric_value": 0.971, "depth": 3}
			if obj[0]>0:
				# {"feature": "Distance", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[10]>1:
					# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[1]<=1:
						# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[2]>0:
							return 'False'
						elif obj[2]<=0:
							# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]<=0:
								return 'False'
							elif obj[4]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[1]>1:
						return 'True'
					else: return 'True'
				elif obj[10]<=1:
					return 'True'
				else: return 'True'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		elif obj[5]>7:
			return 'False'
		else: return 'False'
	elif obj[3]>4:
		return 'True'
	else: return 'True'
