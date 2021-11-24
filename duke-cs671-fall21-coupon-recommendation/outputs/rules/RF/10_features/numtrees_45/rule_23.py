def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Coupon", "instances": 18, "metric_value": 0.9183, "depth": 2}
		if obj[2]<=2:
			# {"feature": "Coffeehouse", "instances": 10, "metric_value": 1.0, "depth": 3}
			if obj[6]<=2.0:
				# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[3]<=0:
					# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[7]<=1.0:
						# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=1.0:
							return 'False'
						elif obj[5]>1.0:
							return 'True'
						else: return 'True'
					elif obj[7]>1.0:
						return 'True'
					else: return 'True'
				elif obj[3]>0:
					return 'False'
				else: return 'False'
			elif obj[6]>2.0:
				return 'True'
			else: return 'True'
		elif obj[2]>2:
			# {"feature": "Passanger", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[0]<=2:
				return 'False'
			elif obj[0]>2:
				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]>0:
					return 'False'
				elif obj[3]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[1]>3:
		return 'True'
	else: return 'True'
