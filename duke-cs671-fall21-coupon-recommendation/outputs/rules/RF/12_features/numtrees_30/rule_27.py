def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Age", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[4]<=4:
		# {"feature": "Coffeehouse", "instances": 26, "metric_value": 0.9957, "depth": 2}
		if obj[8]<=3.0:
			# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Distance", "instances": 12, "metric_value": 0.9183, "depth": 4}
				if obj[11]<=1:
					# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[5]>0:
						# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[1]>1:
							# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[7]<=1.0:
								return 'False'
							elif obj[7]>1.0:
								return 'True'
							else: return 'True'
						elif obj[1]<=1:
							return 'True'
						else: return 'True'
					elif obj[5]<=0:
						return 'False'
					else: return 'False'
				elif obj[11]>1:
					return 'True'
				else: return 'True'
			elif obj[2]>3:
				# {"feature": "Direction_same", "instances": 11, "metric_value": 0.8454, "depth": 4}
				if obj[10]<=0:
					# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[6]<=16:
						return 'False'
					elif obj[6]>16:
						return 'True'
					else: return 'True'
				elif obj[10]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[8]>3.0:
			return 'True'
		else: return 'True'
	elif obj[4]>4:
		return 'True'
	else: return 'True'
