def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Children", "instances": 85, "metric_value": 0.9999, "depth": 1}
	if obj[8]<=0:
		# {"feature": "Coupon", "instances": 50, "metric_value": 0.9427, "depth": 2}
		if obj[3]<=3:
			# {"feature": "Bar", "instances": 29, "metric_value": 0.6632, "depth": 3}
			if obj[12]>1.0:
				return 'True'
			elif obj[12]<=1.0:
				# {"feature": "Gender", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[0]>1:
						# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[10]>3:
							return 'True'
						elif obj[10]<=3:
							return 'False'
						else: return 'False'
					elif obj[0]<=1:
						return 'False'
					else: return 'False'
				elif obj[5]>0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[3]>3:
			# {"feature": "Passanger", "instances": 21, "metric_value": 0.9587, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Distance", "instances": 12, "metric_value": 0.65, "depth": 4}
				if obj[17]>1:
					return 'False'
				elif obj[17]<=1:
					# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[6]<=4:
						return 'True'
					elif obj[6]>4:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[0]>1:
				# {"feature": "Bar", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[12]<=1.0:
					return 'True'
				elif obj[12]>1.0:
					# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[9]>0:
						return 'False'
					elif obj[9]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[8]>0:
		# {"feature": "Coupon", "instances": 35, "metric_value": 0.8981, "depth": 2}
		if obj[3]>0:
			# {"feature": "Occupation", "instances": 28, "metric_value": 0.9666, "depth": 3}
			if obj[10]>6:
				# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.5665, "depth": 4}
				if obj[15]>-1.0:
					return 'False'
				elif obj[15]<=-1.0:
					return 'True'
				else: return 'True'
			elif obj[10]<=6:
				# {"feature": "Education", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[9]<=2:
					# {"feature": "Income", "instances": 10, "metric_value": 0.469, "depth": 5}
					if obj[11]>1:
						return 'True'
					elif obj[11]<=1:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]>1:
							return 'True'
						elif obj[0]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[9]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[3]<=0:
			return 'False'
		else: return 'False'
	else: return 'False'
