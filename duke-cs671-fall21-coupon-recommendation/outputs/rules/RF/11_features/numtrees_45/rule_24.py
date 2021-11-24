def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[2]<=3:
		# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.9183, "depth": 2}
		if obj[7]<=3.0:
			# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.7793, "depth": 3}
			if obj[8]>0.0:
				# {"feature": "Age", "instances": 12, "metric_value": 0.65, "depth": 4}
				if obj[3]>3:
					return 'True'
				elif obj[3]<=3:
					# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[6]<=1.0:
							return 'True'
						elif obj[6]>1.0:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]>1:
								return 'True'
							elif obj[0]<=1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[1]>3:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[8]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[7]>3.0:
			return 'False'
		else: return 'False'
	elif obj[2]>3:
		# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 2}
		if obj[5]<=11:
			return 'False'
		elif obj[5]>11:
			# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[3]<=1:
				return 'True'
			elif obj[3]>1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
