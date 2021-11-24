def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]>0:
		# {"feature": "Coffeehouse", "instances": 19, "metric_value": 0.9819, "depth": 2}
		if obj[7]<=2.0:
			# {"feature": "Occupation", "instances": 16, "metric_value": 0.896, "depth": 3}
			if obj[5]>1:
				# {"feature": "Age", "instances": 10, "metric_value": 1.0, "depth": 4}
				if obj[3]>0:
					# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[0]>0:
						# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[6]>0.0:
							return 'False'
						elif obj[6]<=0.0:
							# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[2]<=0:
								return 'False'
							elif obj[2]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				elif obj[3]<=0:
					return 'True'
				else: return 'True'
			elif obj[5]<=1:
				return 'True'
			else: return 'True'
		elif obj[7]>2.0:
			return 'False'
		else: return 'False'
	elif obj[1]<=0:
		return 'False'
	else: return 'False'
