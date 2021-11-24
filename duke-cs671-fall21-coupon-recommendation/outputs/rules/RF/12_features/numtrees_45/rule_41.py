def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[6]<=8:
		# {"feature": "Age", "instances": 16, "metric_value": 0.9544, "depth": 2}
		if obj[4]>0:
			# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[9]<=2.0:
				# {"feature": "Education", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[5]>1:
					# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[1]>1:
						# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[7]<=0.0:
							return 'False'
						elif obj[7]>0.0:
							return 'True'
						else: return 'True'
					elif obj[1]<=1:
						return 'True'
					else: return 'True'
				elif obj[5]<=1:
					# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[1]<=1:
						return 'False'
					elif obj[1]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[9]>2.0:
				return 'True'
			else: return 'True'
		elif obj[4]<=0:
			return 'True'
		else: return 'True'
	elif obj[6]>8:
		# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[2]>0:
			return 'False'
		elif obj[2]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
