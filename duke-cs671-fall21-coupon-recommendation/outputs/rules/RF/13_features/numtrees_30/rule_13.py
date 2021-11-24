def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Bar", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[8]<=2.0:
		# {"feature": "Coupon", "instances": 27, "metric_value": 0.9911, "depth": 2}
		if obj[2]>0:
			# {"feature": "Passanger", "instances": 23, "metric_value": 0.9986, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Age", "instances": 16, "metric_value": 0.9544, "depth": 4}
				if obj[4]<=2:
					# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[7]>4:
						return 'False'
					elif obj[7]<=4:
						# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[6]>0:
							return 'True'
						elif obj[6]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[4]>2:
					# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[6]<=2:
						# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[7]<=6:
							return 'True'
						elif obj[7]>6:
							# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]<=0:
								return 'True'
							elif obj[1]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[6]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[0]>1:
				# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[7]>1:
					return 'True'
				elif obj[7]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	elif obj[8]>2.0:
		return 'True'
	else: return 'True'
