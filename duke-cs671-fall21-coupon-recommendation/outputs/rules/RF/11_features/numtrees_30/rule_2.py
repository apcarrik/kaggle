def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[5]>2:
		# {"feature": "Passanger", "instances": 29, "metric_value": 0.9991, "depth": 2}
		if obj[0]>0:
			# {"feature": "Coffeehouse", "instances": 26, "metric_value": 0.9829, "depth": 3}
			if obj[7]<=2.0:
				# {"feature": "Age", "instances": 23, "metric_value": 0.9986, "depth": 4}
				if obj[3]>0:
					# {"feature": "Time", "instances": 17, "metric_value": 0.9774, "depth": 5}
					if obj[1]<=2:
						# {"feature": "Bar", "instances": 11, "metric_value": 0.8454, "depth": 6}
						if obj[6]<=2.0:
							# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5436, "depth": 7}
							if obj[9]<=0:
								return 'False'
							elif obj[9]>0:
								# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[4]<=1:
									return 'True'
								elif obj[4]>1:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[6]>2.0:
							# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2]>0:
								# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[4]>0:
									return 'False'
								elif obj[4]<=0:
									return 'True'
								else: return 'True'
							elif obj[2]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[1]>2:
						# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[4]>0:
							# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2]>3:
								return 'False'
							elif obj[2]<=3:
								return 'True'
							else: return 'True'
						elif obj[4]<=0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[3]<=0:
					# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[2]>0:
						return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[7]>2.0:
				return 'True'
			else: return 'True'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	elif obj[5]<=2:
		return 'True'
	else: return 'True'
