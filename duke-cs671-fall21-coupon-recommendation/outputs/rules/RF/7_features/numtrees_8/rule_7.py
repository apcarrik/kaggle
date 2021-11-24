def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Occupation", "instances": 127, "metric_value": 0.9946, "depth": 1}
	if obj[3]<=8.881889763779528:
		# {"feature": "Passanger", "instances": 71, "metric_value": 0.9359, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Distance", "instances": 49, "metric_value": 0.9852, "depth": 3}
			if obj[6]>1:
				# {"feature": "Coupon", "instances": 26, "metric_value": 0.9612, "depth": 4}
				if obj[1]>1:
					# {"feature": "Education", "instances": 18, "metric_value": 1.0, "depth": 5}
					if obj[2]<=0:
						# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.9457, "depth": 6}
						if obj[4]<=1.0:
							# {"feature": "Direction_same", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[5]>0:
								return 'True'
							elif obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[4]>1.0:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[2]>0:
						# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[4]>1.0:
							# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[4]<=1.0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[1]<=1:
					# {"feature": "Education", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[4]<=1.0:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[4]>1.0:
							return 'False'
						else: return 'False'
					elif obj[2]>2:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[6]<=1:
				# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.7554, "depth": 4}
				if obj[4]<=3.0:
					# {"feature": "Direction_same", "instances": 22, "metric_value": 0.684, "depth": 5}
					if obj[5]<=0:
						# {"feature": "Education", "instances": 17, "metric_value": 0.7871, "depth": 6}
						if obj[2]<=2:
							# {"feature": "Coupon", "instances": 15, "metric_value": 0.8366, "depth": 7}
							if obj[1]>0:
								return 'True'
							elif obj[1]<=0:
								return 'False'
							else: return 'False'
						elif obj[2]>2:
							return 'True'
						else: return 'True'
					elif obj[5]>0:
						return 'True'
					else: return 'True'
				elif obj[4]>3.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[0]>2:
			# {"feature": "Distance", "instances": 22, "metric_value": 0.684, "depth": 3}
			if obj[6]>1:
				# {"feature": "Education", "instances": 14, "metric_value": 0.3712, "depth": 4}
				if obj[2]<=2:
					return 'True'
				elif obj[2]>2:
					# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]>0.0:
						# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]<=3:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[4]<=0.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[6]<=1:
				# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[2]<=1:
					# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[1]>2:
						# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]<=1.0:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[1]<=2:
						# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]<=1.0:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[2]>1:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[3]>8.881889763779528:
		# {"feature": "Restaurant20to50", "instances": 56, "metric_value": 0.9769, "depth": 2}
		if obj[4]<=1.0:
			# {"feature": "Education", "instances": 36, "metric_value": 0.9183, "depth": 3}
			if obj[2]>0:
				# {"feature": "Coupon", "instances": 28, "metric_value": 0.9852, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Distance", "instances": 15, "metric_value": 0.7219, "depth": 5}
					if obj[6]<=2:
						# {"feature": "Direction_same", "instances": 10, "metric_value": 0.469, "depth": 6}
						if obj[5]<=0:
							return 'False'
						elif obj[5]>0:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]<=1:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[6]>2:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[1]>2:
					# {"feature": "Passanger", "instances": 13, "metric_value": 0.8905, "depth": 5}
					if obj[0]>2:
						# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[6]>1:
							# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]<=1:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[0]<=2:
						# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[6]<=1:
							return 'True'
						elif obj[6]>1:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		elif obj[4]>1.0:
			# {"feature": "Education", "instances": 20, "metric_value": 0.9928, "depth": 3}
			if obj[2]>0:
				# {"feature": "Coupon", "instances": 15, "metric_value": 0.9968, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Direction_same", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[5]<=0:
						# {"feature": "Passanger", "instances": 8, "metric_value": 1.0, "depth": 6}
						if obj[0]>0:
							# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[6]>1:
								return 'True'
							elif obj[6]<=1:
								return 'False'
							else: return 'False'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					elif obj[5]>0:
						return 'True'
					else: return 'True'
				elif obj[1]>3:
					# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[5]<=0:
						return 'False'
					elif obj[5]>0:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=1:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[2]<=0:
				# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[6]<=1:
					return 'True'
				elif obj[6]>1:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]<=4:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
