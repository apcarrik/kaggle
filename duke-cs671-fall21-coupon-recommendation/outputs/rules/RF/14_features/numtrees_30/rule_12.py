def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Age", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[4]>0:
		# {"feature": "Distance", "instances": 27, "metric_value": 0.9911, "depth": 2}
		if obj[13]<=2:
			# {"feature": "Income", "instances": 23, "metric_value": 0.9986, "depth": 3}
			if obj[8]>1:
				# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.971, "depth": 4}
				if obj[11]<=1.0:
					# {"feature": "Occupation", "instances": 16, "metric_value": 1.0, "depth": 5}
					if obj[7]<=20:
						# {"feature": "Education", "instances": 14, "metric_value": 0.9852, "depth": 6}
						if obj[6]>0:
							# {"feature": "Coupon", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[2]<=2:
								# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[10]>1.0:
									# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[0]<=1:
										return 'True'
									elif obj[0]>1:
										return 'False'
									else: return 'False'
								elif obj[10]<=1.0:
									return 'False'
								else: return 'False'
							elif obj[2]>2:
								return 'True'
							else: return 'True'
						elif obj[6]<=0:
							# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[0]<=1:
								return 'False'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[7]>20:
						return 'True'
					else: return 'True'
				elif obj[11]>1.0:
					return 'True'
				else: return 'True'
			elif obj[8]<=1:
				return 'False'
			else: return 'False'
		elif obj[13]>2:
			return 'False'
		else: return 'False'
	elif obj[4]<=0:
		return 'True'
	else: return 'True'
