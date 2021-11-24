def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Coupon", "instances": 18, "metric_value": 1.0, "depth": 2}
		if obj[2]>0:
			# {"feature": "Bar", "instances": 16, "metric_value": 0.9887, "depth": 3}
			if obj[8]<=1.0:
				# {"feature": "Age", "instances": 14, "metric_value": 1.0, "depth": 4}
				if obj[4]<=6:
					# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9957, "depth": 5}
					if obj[10]>0.0:
						# {"feature": "Education", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[6]>0:
							# {"feature": "Occupation", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[7]>2:
								# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[1]<=1:
									# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[3]<=0:
										return 'True'
									elif obj[3]>0:
										return 'False'
									else: return 'False'
								elif obj[1]>1:
									return 'False'
								else: return 'False'
							elif obj[7]<=2:
								return 'True'
							else: return 'True'
						elif obj[6]<=0:
							return 'False'
						else: return 'False'
					elif obj[10]<=0.0:
						# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[7]>2:
							return 'True'
						elif obj[7]<=2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[4]>6:
					return 'True'
				else: return 'True'
			elif obj[8]>1.0:
				return 'True'
			else: return 'True'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	elif obj[0]>2:
		return 'True'
	else: return 'True'
