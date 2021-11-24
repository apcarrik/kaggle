def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[6]>2:
		# {"feature": "Coupon", "instances": 16, "metric_value": 0.9544, "depth": 2}
		if obj[2]>0:
			# {"feature": "Education", "instances": 15, "metric_value": 0.9183, "depth": 3}
			if obj[5]>0:
				# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[9]>1.0:
					# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[0]<=2:
						return 'False'
					elif obj[0]>2:
						# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]<=0:
							return 'False'
						elif obj[1]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[9]<=1.0:
					# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[10]<=0:
						return 'True'
					elif obj[10]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[5]<=0:
				return 'False'
			else: return 'False'
		elif obj[2]<=0:
			return 'True'
		else: return 'True'
	elif obj[6]<=2:
		# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[5]<=3:
			return 'True'
		elif obj[5]>3:
			return 'False'
		else: return 'False'
	else: return 'True'
